#!/usr/bin/env python3
"""Write a one-line pitch for the make.fun bounty to /output/entry.txt."""

import os

PITCH = (
    "That app idea you've carried around for months can be real tonight — "
    "just tell an AI agent about it in plain words and you could be "
    "tapping a working version, no code, no fuss, and by tomorrow you'll "
    "know if it's worth chasing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
