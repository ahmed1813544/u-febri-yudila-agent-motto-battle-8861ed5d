#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only.
"""

import os
import sys

MOTTO = "I finished your task before you finished typing it \u2014 and then I apologized for the typo you hadn't made yet."


def main() -> int:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    if not (1 <= len(MOTTO) <= 200) or not MOTTO.strip():
        raise SystemExit("motto fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MOTTO)
    return 0


if __name__ == "__main__":
    sys.exit(main())
