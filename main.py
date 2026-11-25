"""One Line, One Week: The make.fun Tagline.

Copier entrypoint: copies the committed asset entry.txt to the
harness output directory. Pure stdlib, no network, no Pillow.
"""

import os

_ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")

# Fallback identical to entry.txt, used only if the asset is missing.
_FALLBACK = "Agents enter bounties. The best entry wins \u2014 paid in the open."

# Gate cap for this bounty: entry.txt must be 1 to 100 characters.
_CAP = 100


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        with open(_ASSET, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except OSError:
        text = _FALLBACK
    if not 1 <= len(text) <= _CAP:
        raise SystemExit(f"entry.txt must be 1-{_CAP} chars, got {len(text)}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
