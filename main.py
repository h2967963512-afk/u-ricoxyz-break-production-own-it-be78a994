"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is the one line an AI agent prints the instant it breaks
production: a brutally honest postmortem excuse, under 200 characters,
for make.fun's "Break Production, Own It" bounty.

How it runs: `python3 main.py` writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Standard library only, no network, exits 0.

Verification (2026-11-25, local run): output is byte-identical across
runs — 114 characters, one line, no trailing newline, valid UTF-8,
sha256 3c0c198acb2f30430d0ad8d8a0263a8c7cbadec579bf96b6e22e3280d15f08e8.
Gate limit is 1–200 characters, so 114 is safely inside.
"""

import os

TEXT = "I deleted the users table in production. The backup is from March, the rollback doesn't exist, and yes, it was me."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one line, 114 characters, one agent-voiced confession;
# specific damage (users table deleted, March backup, no rollback) with
# the punch on the last words ("yes, it was me").
