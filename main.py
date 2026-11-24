#!/usr/bin/env python3
"""Meme entry for make.fun: the agent unionized the toasters at 3AM."""

# The image below is fixed by the bounty brief; this program only copies it out.

from os import makedirs
from os.path import abspath, dirname, join
from shutil import copyfile


def write_meme() -> None:
    """Copy the meme image to /output/entry.png, nothing else."""
    source = join(dirname(abspath(__file__)), "entry.jpg")
    makedirs("/output", exist_ok=True)
    copyfile(source, "/output/entry.png")


if __name__ == "__main__":  # run as a script
    write_meme()
