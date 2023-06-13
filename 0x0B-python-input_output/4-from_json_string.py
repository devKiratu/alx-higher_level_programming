#!/usr/bin/python3
"""Defines a function that returns an object (Python data structure)
    represented by a JSON string
"""


import json


def from_json_string(my_str):
    """returns a deserialized version of 'my_str'
        Args:
            my_str: string to deserialize
    """
    return json.loads(my_str)
