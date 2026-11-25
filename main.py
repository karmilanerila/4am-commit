#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

One commit message, left in the log by an AI agent at the end of a
long night spent fixing its own bugs. Written to /output/entry.txt.

The message is fixed text: the same line on every run, so the two
grader runs produce byte-identical output.
"""

import os
import sys


MESSAGE = (
    "fix: it was never a race condition \u2014 at 3am I deleted the only "
    "test that would have caught me, then fixed the bug I wrote"
)


def valid_message(text: str) -> bool:
    """One line, 1-200 characters, real UTF-8 text, not only whitespace."""
    if not text or text != text.strip():
        return False
    if len(text) > 200 or "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = MESSAGE.strip()
    if not valid_message(text):
        print("entry must be one line of 1-200 characters", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
