#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a single line: the agent insists a bug cannot be
reproduced, then reproduces it in the one place it matters most.
"""

import os

JOKE = "My agent said the bug was impossible to reproduce, so it reproduced it in production."

def main():
    # Gate: /output/entry.txt must be 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280, "joke outside the 1-280 code point gate"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must land in one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
