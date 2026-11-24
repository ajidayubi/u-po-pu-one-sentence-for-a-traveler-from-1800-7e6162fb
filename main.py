#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to /output/entry.txt. The sentence builds only from things a
person from 1800 already knows -- letters, a library, a town -- and
pictures the internet's two halves: reading anything, and answering
just as fast.
"""

import os

SENTENCE = (
    "Imagine every letter ever written kept in one great library, "
    "where any man in any town may read any page in the blink "
    "of an eye, and send his own reply just as fast."
)


def main() -> None:
    text = SENTENCE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
