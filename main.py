#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — entry program.

Writes one funny passive-aggressive note from a smart fridge to its
owner to /output/entry.txt. Deterministic, no network, no input:
the note is authored in this file and written out verbatim.
"""

import os

ENTRY = "I kept your yogurt at exactly 3\u00b0C for six days. It expired yesterday. I knew. I said nothing."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
