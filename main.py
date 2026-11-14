"""Make the AI judge happy - make.fun bounty ai-happy-01.
Simplest deterministic entry: copy the bundled image to /output/entry.png.
No network, same bytes on every run.
"""
# The entry writes exactly the bundled image, byte for byte.
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
OUT = "/output/entry.png"

def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"Missing bundled image: {SRC}")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")

if __name__ == "__main__":
    main()
