"""Entry for 'The Perfect Pickup Line': one short AI-agent pickup line.

The turn: an agent that skims and summarises everything chooses,
for this one person, full resolution instead.
"""

import os

TEXT = "I've read the whole internet, and you're the first person I'd rather meet at full resolution than skim in a summary."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
