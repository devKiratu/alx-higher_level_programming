#!/usr/bin/python3
"""Defines base class for all the classes in this project"""


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
