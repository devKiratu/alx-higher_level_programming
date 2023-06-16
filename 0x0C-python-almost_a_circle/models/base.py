#!/usr/bin/python3
"""Defines base class for all the classes in this project"""


import json


class Base:
    """Base class - manages the id attribute in all subclasses"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the id attribute"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if isinstance(list_dictionaries, list):
            return json.dumps(list_dictionaries)
