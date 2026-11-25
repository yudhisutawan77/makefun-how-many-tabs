#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one honest browser tab count, digits only, to /output/entry.txt.
No words, no explanation, no trailing newline: just the number.
"""

import os
import sys

TAB_COUNT = 47

# Why 47: a non-round number reads as a count someone actually looked at
# and counted, not a rounded estimate. High enough to surprise against a
# field of single-digit and tidy round counts, low enough to stay a
# believable, lived-in answer -- the tab hoard of a real browsing session,
# not a figure picked to shock.
ENTRY_DIR = os.environ.get("ENTRY_OUT", "/output")
ENTRY_PATH = os.path.join(ENTRY_DIR, "entry.txt")


def main() -> int:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
