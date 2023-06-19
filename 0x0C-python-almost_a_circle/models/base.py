#!/usr/bin/python3
"""Defines base class for all the classes in this project"""


import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as f:
                json_str = f.read()
                objs_list = cls.from_json_string(json_str)
                instances = []
                for obj in objs_list:
                    instances.append(cls.create(**obj))
                return instances
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes object to csv
            Args:
                list_objs: objects to serialize to csv
        """
        filename = "{}.csv".format(cls.__name__)
        if list_objs is None:
            data = []
        if cls.__name__ == "Rectangle":
            data = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                    for obj in list_objs]
        if cls.__name__ == "Square":
            data = [[obj.id, obj.size, obj.x, obj.y]
                    for obj in list_objs]
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a csv file into Rectangle/Square instances"""
        filename = "{}.csv".format(cls.__name__)
        try:
            data = []
            with open(filename, newline="") as f:
                rows = csv.reader(f)
                for row in rows:
                    num_row = [int(i) for i in row]
                    if cls.__name__ == "Rectangle":
                        r_id, width, height, x, y = num_row
                        kwargs = {'id': r_id, 'width': width,
                                  'height': height, 'x': x, 'y': y}
                    elif cls.__name__ == "Square":
                        s_id, size, x, y = num_row
                        kwargs = {'id': s_id, 'size': size, 'x': x, 'y': y}
                    obj = cls.create(**kwargs)
                    data.append(obj)
            return data
        except Exception:
            return []
