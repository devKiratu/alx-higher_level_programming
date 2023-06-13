#!/usr/bin/python3
"""Contains function for reading text files"""


def read_file(filename=""):
    """reads file and prints out to the standard output
        Args:
            filename: file to read
    """
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
        print(contents)
