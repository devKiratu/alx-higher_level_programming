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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
            Args:
                list_objs: objects to write to file
        """
        filename = "{}.json".format(cls.__name__)
        if isinstance(list_objs, list):
            if len(list_objs) > 0:
                filename = "{}.json".format(list_objs[0].__class__.__name__)
                if all(isinstance(obj, cls) for obj in list_objs):
                    data = cls.to_json_string(
                            [obj.to_dictionary() for obj in list_objs]
                            )
                else:
                    data = cls.to_json_string(list_objs)
        else:
            data = cls.to_json_string([])
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
            Args:
                json_string: a string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
            Args:
                dictionary: key word arguments/attributes for instance
        """
        dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy
