#!/usr/bin/python3
"""Contains function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes text to filename
        Args:
            filename: file to write to
            text: string to write to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
