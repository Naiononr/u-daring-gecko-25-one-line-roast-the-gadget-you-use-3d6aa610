#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day
(u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

Writes one original roast line about a gadget used every day to
/output/entry.txt. Python 3.13, standard library only, fully
deterministic: the line is a fixed string in this source, no network,
no randomness, no time dependence.

Gate (per the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space.

The file is written world-readable (mode 0644): the scorer must be able
to read it. Locally, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = (
    "My robot vacuum owns a perfect map of my flat and still wedges itself "
    "under the same sofa every day — the smartest gadget in my house is "
    "also the dumbest."
)

if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"line must be 1-200 characters, got {len(LINE)}")
if not LINE.strip():
    raise SystemExit("line must not be only white space")

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
