#!/usr/bin/env python3
"""Writes the single-line office joke entry to /output/entry.txt."""
import os

LINE = "I asked my calendar for work-life balance; it reply-all'd a recurring 9am 'Synergy Alignment' and marked my attendance optional."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
