#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes a single digit -- the honest count of open browser tabs -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The count is 1: one tab open, one thing at a time. Logged browser data,
not self-report, says the most common number of tabs to have open is
one (Dubroy & Balakrishnan, 2010), and only about 9% of people have one
or no tabs open -- so a single tab is both real and far lower than the
field will guess. The field will chase big numbers; the low end is
where the surprise lives.
"""

import os
import sys

ENTRY = "1"


def output_path():
    """Resolve the output file location.

    The grader sets MAKEFUN_OUTPUT_DIR; local runs fall back to
    /output, and if that is not writable, to a local ./output dir.
    """
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(base, exist_ok=True)
    except OSError:
        base = os.path.join(os.getcwd(), "output")
        os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def validate(entry):
    """Check the entry against the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 5
    characters, not only white space; the task adds digits only, one
    number, no words, no punctuation.
    """
    if not entry:
        raise ValueError("entry is empty")
    if len(entry) > 5:
        raise ValueError("entry is longer than 5 characters")
    if not entry.isdigit():
        raise ValueError("entry must be digits only")
    if not entry.strip():
        raise ValueError("entry must not be whitespace only")


def main():
    validate(ENTRY)
    path = output_path()
    # Exactly one character, no trailing newline: the file holds the
    # number and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    print(f"wrote {ENTRY!r} to {path}")


if __name__ == "__main__":
    main()
