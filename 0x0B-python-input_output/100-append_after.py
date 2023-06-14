#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """insert 'new_string' after a line containing 'search_string'
        Args:
            filename: file to read/append text
            search_string: string to look for in a line
            new_string: string to append to line after line
            containing search_string
    """
    text = []
    with open(filename, "r", encoding="utf-8") as f:
        text = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
