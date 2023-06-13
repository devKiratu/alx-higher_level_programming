#!/usr/bin/python3
"""Defines a function that writes an Object to a text file,
    using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """serializes my_obj and saves it in filename
        Args:
            my_obj: object to serialize
            filename: file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
