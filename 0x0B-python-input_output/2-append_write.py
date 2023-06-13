#!/usr/bin/python3
"""Contains function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends text at the end of filename,
        returns number of characters written
        Args:
            filename: file to write to
            text: string to append to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
