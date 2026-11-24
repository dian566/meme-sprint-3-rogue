"""Meme Sprint 3: AI Agent Goes Rogue — make.fun entry.

Writes the meme image to /output/entry.png.
"""

import os
import shutil

def main():
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
    shutil.copyfile(src, "/output/entry.png")

if __name__ == "__main__":
    main()
