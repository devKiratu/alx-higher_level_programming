#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student by first name, last name and age"""
    def __init__(self, first_name, last_name, age):
        """initialize the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a filtered dictionary representation of a Student
            based on the attrs list
            Args:
                attrs: list of attributes to retrieve
        """
        result = self.__dict__
        if attrs is None:
            return result
        return dict(filter((lambda pair: pair[0] in attrs), result.items()))

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
            Args:
                json: dictionary containing new attributes
        """
        for pair in json.items():
            setattr(self, pair[0], pair[1])
