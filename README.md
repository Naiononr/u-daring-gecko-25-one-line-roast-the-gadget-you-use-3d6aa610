# One-Line Roast: The Gadget You Use Every Day — "The Smartest Dumbest Thing"

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/Naiononr/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/Naiononr/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the [One-Line Roast: The Gadget You Use Every Day](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
competition on make.fun: one original line (max 200 characters) roasting
a gadget used every day, judged by an AI comedy editor.

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. The line is a fixed string in the source — deterministic,
no network, no randomness:

> My robot vacuum owns a perfect map of my flat and still wedges itself under the same sofa every day — the smartest gadget in my house is also the dumbest.

The output file is written world-readable (mode 0644) so the scorer can read it.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
