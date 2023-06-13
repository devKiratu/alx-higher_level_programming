#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """loads an object from file 'filename'
        Args:
            filename: file to load object from
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
