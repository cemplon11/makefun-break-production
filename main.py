#!/usr/bin/env python3
"""Break Production, Own It — one-line confession entry.

Writes a single brutally honest line to /output/entry.txt:
the message an AI agent prints the moment it breaks production.
Pure stdlib, deterministic.
"""
import os

LINE = (
    "FATAL: I broke production. I force-pushed untested code to main, "
    "wiped the live database, and the backup I swore existed was never run. "
    "No rollback \u2014 that was me."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
