#!/usr/bin/python3
"""Defines function that returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """returns the serialized object"""
    return json.dumps(my_obj)
