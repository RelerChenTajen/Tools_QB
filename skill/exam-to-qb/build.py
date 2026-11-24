#!/usr/bin/env python3
"""
build.py - Convert a TSV of parsed exam questions into question-bank CSV format.

Cross-platform port of build.ps1 (Windows PowerShell). Byte-for-byte compatible
output. Runs on any host with Python 3.7+, so the skill works under Claude Code,
OpenAI Codex and Gemini CLI on Windows, macOS and Linux alike.

Pipeline contract:
  - The agent parses the source document into questions and writes a TSV file.
  - This script applies the 27-column question-bank template header + CSV
    escaping, and writes the final CSV as UTF-8 (no BOM).
  - This script is intentionally ASCII-only so its own encoding is never an
    issue; all CJK content lives in the TSV and header.csv (read as UTF-8).

TSV format (one question per line, fields separated by a literal TAB):
  [0] type       1=true/false 2=single 3=multiple 4=fill-in 5=essay
  [1] question   question text
  [2] answer     T/F -> 1(yes) or 2(no)
                 single -> option number (e.g. 2)
                 multiple -> comma-joined numbers, e.g. 1,2,4 (script quotes it)
                 fill-in -> leave EMPTY; embed answers inline as [*answer*]
                 essay -> reference answer text
  [3] explanation  optional
  [4] difficulty   1=easy 2=medium 3=hard
  [5] option1    choices: option 1 text; fill-in: 1=ignore case 2=match case
  [6] option2    choices: option 2 text; fill-in: 1=any order 2=keep order
  [7..] option3.. additional choice options

Encode newlines inside any field as the two-character token \n ; the script
turns them into real CRLF inside a quoted CSV field.

Usage:
  python build.py --tsv rows.tsv --out exam02.csv
                  [--header header.csv] [--category NAME | --category-file F]
                  [--big5] [--big5-out PATH] [--allow-invalid]

  --category       one category applied to every row (column 2)
  --category-file  a text file with ONE category per line, matched to the TSV
                   rows in order (for sources whose sections differ per block)
  --big5           also emit a Big5 (cp950) copy; default path inserts "_big5"
                   before the extension
  --allow-invalid  write the CSV even if validation finds errors (they are
                   still listed); use only when the source itself is incomplete

Validation: every row is checked before anything is written. Errors (bad type,
empty question, bad difficulty, answer missing or pointing at a nonexistent
option, malformed fill-in, too many columns) are all listed and stop the run
with exit code 1 and no output. Doubtful but legal rows (multiple-choice with
one answer, essay without reference answer) only produce warnings. A well-formed
but wrong answer cannot be detected here; compare with the source.

Big5 note: cp950 has a smaller repertoire than UTF-8. A few characters are
remapped to Big5 equivalents (see REMAP below). Any character that still cannot
be encoded is written as '?' and reported as a warning, so the operator can
decide whether the Big5 copy is acceptable.
"""
import argparse
import os
import re
import sys

# Characters with a Big5-friendly equivalent. Applied only to the Big5 copy.
REMAP = {
    "\u2265": "\u2267",  # >=
    "\u2264": "\u2266",  # <=
    "\u30fb": "\u2027",  # katakana middle dot -> hyphenation point
}

# The two-character token (backslash + n) that a TSV field uses to mean "newline".
# Spelled with chr(92) so the literal survives any copy/paste or shell quoting.
NL_TOKEN = chr(92) + "n"

SPLIT_LINES = re.compile(r"\r\n|\r|\n")
NEEDS_QUOTE = re.compile(r'["\r\n,]')

OPTION_NO = re.compile(r"[1-9][0-9]*$", re.ASCII)
FILL_BLANK = re.compile(r"\[\*.+?\*\]")
MAX_FIELDS = 25  # 5 leading fields + 20 options


def read_text(path):
    with open(path, "rb") as fh:
        data = fh.read()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    return data.decode("utf-8")


def read_lines(path):
    text = read_text(path)
    return SPLIT_LINES.split(text)


def esc(value):
    if value is None:
        value = ""
    value = value.replace(NL_TOKEN, "\r\n")
    if NEEDS_QUOTE.search(value):
        return '"' + value.replace('"', '""') + '"'
    return value


def check_row(fields):
    """Return (errors, warnings) for one TSV row."""
    errors, warnings = [], []
    if len(fields) > MAX_FIELDS:
        errors.append(
            "has %d fields, limit %d (stray TAB?)" % (len(fields), MAX_FIELDS)
        )
    padded = (fields + [""] * MAX_FIELDS)[:MAX_FIELDS]
    qtype, question, answer, _, difficulty = padded[:5]
    options = padded[5:]

    if qtype not in ("1", "2", "3", "4", "5"):
        errors.append("type must be 1-5, got %a" % qtype)
    if not question.strip():
        errors.append("question is empty")
    if difficulty not in ("1", "2", "3"):
        errors.append("difficulty must be 1-3, got %a" % difficulty)

    if qtype == "1":
        if answer not in ("1", "2"):
            errors.append("true/false answer must be 1 or 2, got %a" % answer)
    elif qtype in ("2", "3"):
        picks = answer.split(",") if answer else []
        if not picks:
            errors.append("answer is missing")
        elif qtype == "2" and len(picks) != 1:
            errors.append("single choice needs exactly one answer, got %a" % answer)
        elif qtype == "3" and len(picks) == 1:
            warnings.append("multiple choice has only one answer")
        if len(set(picks)) != len(picks):
            errors.append("answer repeats an option: %a" % answer)
        for pick in picks:
            if not OPTION_NO.match(pick):
                errors.append("answer %a is not an option number" % pick)
            elif int(pick) > len(options) or not options[int(pick) - 1].strip():
                errors.append("answer %s points to an empty option" % pick)
    elif qtype == "4":
        if answer:
            errors.append("fill-in answer column must be empty")
        if not FILL_BLANK.search(question):
            errors.append("fill-in question has no [*answer*]")
        if options[0] not in ("1", "2") or options[1] not in ("1", "2"):
            errors.append("fill-in option1/option2 flags must be 1 or 2")
    elif qtype == "5":
        if not answer.strip():
            warnings.append("essay has no reference answer")
    return errors, warnings


def validate(tsv_path, allow_invalid):
    n = bad = 0
    for line in read_lines(tsv_path):
        if not line.strip():
            continue
        n += 1
        errors, warnings = check_row(line.split("\t"))
        bad += bool(errors)
        for msg in errors:
            print("INVALID question %d: %s" % (n, msg))
        for msg in warnings:
            print("WARN question %d: %s" % (n, msg))
    if n == 0:
        sys.exit("ERROR: the TSV has no questions")
    if bad and not allow_invalid:
        sys.exit(
            "ERROR: %d of %d questions are invalid; nothing was written" % (bad, n)
        )
    if bad:
        print("WARN: writing anyway, %d of %d questions are invalid" % (bad, n))


def build_rows(tsv_path, categories):
    rows = []
    idx = 0
    for line in read_lines(tsv_path):
        if not line.strip():
            continue
        fields = line.split("\t")
        if categories is None:
            category = ""
        elif isinstance(categories, str):
            category = categories
        else:
            if idx >= len(categories):
                sys.exit(
                    "ERROR: category file has %d lines but the TSV has more rows"
                    % len(categories)
                )
            category = categories[idx]
        cols = ["", category] + fields
        cols = (cols + [""] * 27)[:27]
        rows.append(",".join(esc(c) for c in cols))
        idx += 1
    if isinstance(categories, list) and idx != len(categories):
        sys.exit(
            "ERROR: category file has %d lines but the TSV has %d rows"
            % (len(categories), idx)
        )
    return rows


def write_big5(content, path):
    remapped = content
    for src, dst in REMAP.items():
        remapped = remapped.replace(src, dst)

    bad = set()
    for ch in remapped:
        if ord(ch) < 32:
            continue
        try:
            ch.encode("cp950")
        except UnicodeEncodeError:
            bad.add("%s(U+%04X)" % (ch, ord(ch)))

    with open(path, "wb") as fh:
        fh.write(remapped.encode("cp950", errors="replace"))

    size = os.path.getsize(path)
    if bad:
        print(
            "WARN -> %s  (Big5/cp950)  bytes=%d  UNMAPPABLE chars replaced "
            "with '?': %s" % (path, size, ", ".join(sorted(bad)))
        )
    else:
        print("OK -> %s  (Big5/cp950, lossless)  bytes=%d" % (path, size))


def main():
    ap = argparse.ArgumentParser(description="TSV -> question-bank CSV")
    ap.add_argument("--tsv", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--header")
    ap.add_argument("--category", default="")
    ap.add_argument("--category-file", dest="category_file")
    ap.add_argument("--big5", action="store_true")
    ap.add_argument("--big5-out", dest="big5_out", default="")
    ap.add_argument("--allow-invalid", dest="allow_invalid", action="store_true")
    args = ap.parse_args()

    header_path = args.header or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "header.csv"
    )
    header = read_text(header_path).rstrip("\r\n")

    if args.category_file:
        if args.category:
            sys.exit("ERROR: use either --category or --category-file, not both")
        categories = [
            ln for ln in read_lines(args.category_file) if ln.strip() != ""
        ]
        label = "<per-row: %d>" % len(categories)
    else:
        categories = args.category
        label = args.category

    validate(args.tsv, args.allow_invalid)
    rows = build_rows(args.tsv, categories)
    content = header + "\r\n" + "\r\n".join(rows) + "\r\n"

    with open(args.out, "wb") as fh:
        fh.write(content.encode("utf-8"))

    data = open(args.out, "rb").read()
    has_bom = data[:3] == b"\xef\xbb\xbf"
    print(
        "OK -> %s  rows=%d  category='%s'  bytes=%d  BOM=%s"
        % (args.out, len(rows), label, len(data), has_bom)
    )

    if args.big5 or args.big5_out:
        big5_out = args.big5_out
        if not big5_out:
            root, ext = os.path.splitext(args.out)
            big5_out = root + "_big5" + ext
        write_big5(content, big5_out)


if __name__ == "__main__":
    main()
