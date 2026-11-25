#!/usr/bin/env python3
"""
pack.py - Build the web-upload ZIPs from the canonical skill (skill/exam-to-qb).

  dist/exam-to-qb.zip         exam-to-qb/SKILL.md ...  Claude Web, ChatGPT Web
  dist/exam-to-qb-gemini.zip  SKILL.md only             Gemini Web

Gemini Web refuses to run scripts in custom skills (seen 2026-11-25), so its
package is instructions only and Gemini writes the 27-column CSV itself. That
SKILL.md comes from gemini/SKILL.template.md, with the format table, parsing
rules and CSV header filled in from the canonical skill.

Usage:
  python web/pack.py           # rebuild both ZIPs
  python web/pack.py --check   # exit 1 if the ZIPs are out of date
"""
import csv
import io
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "skill", "exam-to-qb")
DIST = os.path.join(HERE, "dist")
TEMPLATE = os.path.join(HERE, "gemini", "SKILL.template.md")

# build.ps1 (Windows only) and examples/ are not needed on the web.
FILES = ["SKILL.md", "build.py", "extract.py", "header.csv"]

# Gemini template placeholder -> the canonical SKILL.md section that fills it.
SHARED = {
    "{{QB_FORMAT}}": re.compile(r"^## [^\n]*27[^\n]*\n(.*?)\n(?=## )", re.M | re.S),
    "{{PARSE_RULES}}": re.compile(r"^### 2\. [^\n]*\n(.*?)\n(?=### )", re.M | re.S),
}


TSV_NEWLINE_RULE = "多行用 `\\n` 標記（見下）。"
CSV_NEWLINE_RULE = "多行直接在雙引號內換行。"


def payload(name):
    with open(os.path.join(SRC, name), "rb") as fh:
        data = fh.read()
    # header.csv line endings are significant: ship it byte for byte.
    if not name.endswith(".csv"):
        data = data.replace(b"\r\n", b"\n")
    return data


def gemini_skill(canonical, header):
    with open(TEMPLATE, "rb") as fh:
        text = fh.read().replace(b"\r\n", b"\n").decode("utf-8")
    for mark, pattern in SHARED.items():
        found = pattern.search(canonical)
        if not found or text.count(mark) != 1:
            sys.exit("ERROR: cannot fill %s" % mark)
        text = text.replace(mark, found.group(1).strip("\n"))
    # The canonical rules use a \n token for the TSV step; here Gemini writes
    # real line breaks inside quoted CSV fields.
    if text.count(TSV_NEWLINE_RULE) != 1:
        sys.exit("ERROR: TSV newline rule not found; update TSV_NEWLINE_RULE")
    text = text.replace(TSV_NEWLINE_RULE, CSV_NEWLINE_RULE)
    header = header.decode("utf-8").replace("\r\n", "\n").rstrip("\n")
    text = text.replace("{{HEADER}}", header)
    if "{{" in text:
        sys.exit("ERROR: unfilled placeholder in the Gemini template")
    check_templates(text)
    return text.encode("utf-8")


def check_templates(skill_md):
    """Every sample row in the Gemini skill must really have 27 columns."""
    blocks = re.findall(r"^```\n(,.*?)\n```$", skill_md, re.M | re.S)
    for block in blocks:
        rows = list(csv.reader(io.StringIO(block, newline="")))
        if len(rows) != 1 or len(rows[0]) != 27:
            sys.exit("ERROR: template row is not 27 columns: %a" % block[:60])
    if len(blocks) < 5:
        sys.exit("ERROR: expected a template row per question type")


def check_frontmatter(text):
    name = re.search(r"^name: *(.+)$", text, re.M).group(1).strip()
    desc = re.search(r"^description: *(.+)$", text, re.M).group(1).strip()
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
        sys.exit("ERROR: bad skill name: %s" % name)
    if len(desc) > 200:  # Claude Web has the tightest limit
        sys.exit("ERROR: description is %d chars, limit 200" % len(desc))


def main():
    wanted = {f: payload(f) for f in FILES}
    canonical = wanted["SKILL.md"].decode("utf-8")
    gemini = gemini_skill(canonical, wanted["header.csv"])
    check_frontmatter(canonical)
    check_frontmatter(gemini.decode("utf-8"))
    packages = {
        "exam-to-qb.zip": {"exam-to-qb/" + f: d for f, d in wanted.items()},
        "exam-to-qb-gemini.zip": {"SKILL.md": gemini},
    }
    stale = False
    for pkg, expect in packages.items():
        path = os.path.join(DIST, pkg)
        if "--check" in sys.argv:
            actual = {}
            if os.path.exists(path):
                with zipfile.ZipFile(path) as zf:
                    actual = {n: zf.read(n) for n in zf.namelist()}
            ok = actual == expect
            stale = stale or not ok
            print("%s  %s" % ("OK   " if ok else "STALE", pkg))
            continue
        os.makedirs(DIST, exist_ok=True)
        with zipfile.ZipFile(path, "w") as zf:
            for name, data in expect.items():
                info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o644 << 16
                zf.writestr(info, data)
        print("OK -> %s" % pkg)
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
