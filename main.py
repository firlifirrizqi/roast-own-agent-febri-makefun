#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast entry for Make.fun.

The program writes a single original roast of my own AI agent to
/output/entry.txt, exactly as the bounty requires.
"""

import os

MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_PATH = "/output/entry.txt"

ROAST = (
    "Rika says 'let me verify that', verifies it twice, logs the "
    "verification, and the tool call she promised is still loading."
)


def verify_output() -> None:
    """Read back /output/entry.txt and confirm it is byte-identical."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ROAST, "entry.txt does not match the roast line exactly"
    assert written.encode("utf-8") == ROAST.encode("utf-8")


def main() -> None:
    # The gate allows 1 to 200 characters, not only white space.
    assert MIN_CHARS <= len(ROAST) <= MAX_CHARS, f"roast is {len(ROAST)} chars"
    assert ROAST.strip(), "roast must not be only white space"
    assert "\n" not in ROAST, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)
    verify_output()


if __name__ == "__main__":
    main()
