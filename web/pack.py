#!/usr/bin/env python3
"""
pack.py - Build the web-upload ZIPs from the canonical skill (skill/exam-to-qb).

  dist/exam-to-qb.zip         exam-to-qb/SKILL.md ...  Claude Web, ChatGPT Web
  dist/exam-to-qb-gemini.zip  SKILL.md ... at ZIP root  Gemini Web

Usage:
  python web/pack.py           # rebuild both ZIPs
  python web/pack.py --check   # exit 1 if the ZIPs are out of date
"""
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "skill", "exam-to-qb")
DIST = os.path.join(HERE, "dist")

# build.ps1 (Windows only) and examples/ are not needed on the web.
FILES = ["SKILL.md", "build.py", "extract.py", "header.csv"]
PACKAGES = {"exam-to-qb.zip": "exam-to-qb/", "exam-to-qb-gemini.zip": ""}


def payload(name):
    with open(os.path.join(SRC, name), "rb") as fh:
        data = fh.read()
    # header.csv line endings are significant: ship it byte for byte.
    if not name.endswith(".csv"):
        data = data.replace(b"\r\n", b"\n")
    return data


def check_frontmatter(text):
    name = re.search(r"^name: *(.+)$", text, re.M).group(1).strip()
    desc = re.search(r"^description: *(.+)$", text, re.M).group(1).strip()
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
        sys.exit("ERROR: bad skill name: %s" % name)
    if len(desc) > 200:  # Claude Web has the tightest limit
        sys.exit("ERROR: description is %d chars, limit 200" % len(desc))


def main():
    wanted = {f: payload(f) for f in FILES}
    check_frontmatter(wanted["SKILL.md"].decode("utf-8"))
    stale = False
    for pkg, prefix in PACKAGES.items():
        path = os.path.join(DIST, pkg)
        expect = {prefix + f: d for f, d in wanted.items()}
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
