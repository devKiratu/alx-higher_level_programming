#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student by first name, last name and age"""
    def __init__(self, first_name, last_name, age):
        """initialize the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
