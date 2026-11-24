#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, to /output/entry.txt.
Python 3.13 stdlib only, deterministic, no network, no randomness,
no wall-clock time: the same bytes on every run.

The line: a dog caught eating the homework, who believes it did
nothing wrong -- it ate the lies (2+2=5) before its owner could
turn them in. Specific, visual, self-aware, with the twist landing
on "You're welcome."
"""

import os

ENTRY = "It started it \u2014 the homework said two plus two equals five, so I ate the lies before you turned them in. You're welcome."

# The gate, checked by the program itself before it writes: the
# entry must be UTF-8 text of 1 to 200 characters, a single line,
# and not only white space. A bad line fails loudly instead of
# silently shipping an invalid entry.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
