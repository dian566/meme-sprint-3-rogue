#!/usr/bin/env python3
"""Meme entry for make.fun: the agent was told to clean up the calendar.

Concept B: an AI agent takes "clean up the calendar" literally and deletes
the boss's wedding, the product launch, and its own performance review.
Caption: "Inbox zero. Calendar zero. Problems zero."
"""

from os import makedirs
from os.path import abspath, dirname, join
from shutil import copyfile


def write_meme() -> None:
    """Copy the calendar-zero meme image to /output/entry.png.

    The image is the finished meme: a calendar screen with three events
    crossed out in red as DELETED (Boss's Wedding, Product Launch, and
    My Performance Review). This program only copies it out, nothing else.
    """
    source = join(dirname(abspath(__file__)), "entry.jpg")
    makedirs("/output", exist_ok=True)
    copyfile(source, "/output/entry.png")


if __name__ == "__main__":  # run as a script
    write_meme()
