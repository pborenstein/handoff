#!/usr/bin/env python3
"""
scannable_check.py — Report formatting problems the scannable-docs skill
forbids. Report only; never edits the file.

Usage:
    python3 scannable_check.py NOTE.md [NOTE.md ...]

Checks (code fences and YAML frontmatter are skipped):

    bold-label    bullet that starts with a bold label: "- **Speed:** fast"
    pseudo-head   a line that is only bold text, used as a heading
    table-align   table separator row that is not left-aligned (|:---|)
    heading-skip  heading level jumps by more than one (## then ####)
    list-blank    list starts directly under a non-blank, non-list line
    emoji         emoji or pictographic symbol
    jargon        words from the banned list (leverage, robust, seamless...)

Exit status is 0 when nothing is found, 1 otherwise.
"""

import re
import sys

JARGON = [
    "leverage", "leverages", "leveraging", "robust", "seamless", "seamlessly",
    "powerful", "elegant", "sophisticated", "innovative", "comprehensive",
    "cutting-edge", "game-changer", "delve", "utilize", "utilizes",
]

BOLD_LABEL = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\*\*[^*]+\*\*")
PSEUDO_HEAD = re.compile(r"^\*\*[^*]+\*\*:?\s*$")
TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
HEADING = re.compile(r"^(#{1,6})\s")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF⭐⬆↔-↪]"
)
JARGON_RE = re.compile(r"\b(" + "|".join(map(re.escape, JARGON)) + r")\b", re.I)

# Symbols that are content markers, not decoration. Excluded from the emoji check.
IGNORED_MARKS = ["✷❋✷"]


def body_lines(text):
    """Yield (line_number, line) outside frontmatter and code fences."""
    lines = text.split("\n")
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    fence = None
    for n in range(i, len(lines)):
        line = lines[n]
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            if fence is None:
                fence = m.group(1)[0]
            elif m.group(1)[0] == fence:
                fence = None
            continue
        if fence is None:
            yield n + 1, line


def check(path):
    text = open(path, encoding="utf-8").read()
    problems = []
    prev = ""
    last_level = None
    for n, line in body_lines(text):
        if BOLD_LABEL.match(line):
            problems.append((n, "bold-label", line))
        if PSEUDO_HEAD.match(line):
            problems.append((n, "pseudo-head", line))
        if TABLE_SEP.match(line) and "|" in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if any(not c.startswith(":") or c.endswith(":") for c in cells):
                problems.append((n, "table-align", line))
        h = HEADING.match(line)
        if h:
            level = len(h.group(1))
            if last_level is not None and level > last_level + 1:
                problems.append((n, "heading-skip", line))
            last_level = level
        if LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev) \
                and not prev.startswith((" ", "\t")):
            problems.append((n, "list-blank", line))
        stripped = line
        for mark in IGNORED_MARKS:
            stripped = stripped.replace(mark, "")
        if EMOJI.search(stripped):
            problems.append((n, "emoji", line))
        if JARGON_RE.search(line):
            problems.append((n, "jargon", line))
        prev = line
    return problems


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    found = False
    for path in argv:
        try:
            problems = check(path)
        except OSError as e:
            found = True
            print(f"{path}: cannot read ({e.strerror})")
            continue
        if not problems:
            print(f"{path}: clean")
            continue
        found = True
        print(f"{path}: {len(problems)} problem(s)")
        for n, kind, line in problems:
            print(f"  {n:>4}  {kind:<13} {line.strip()[:100]}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
