#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """Geometry Base class"""
    def area(self):
        """Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
            Args:
                name: name of value
                value: value to vaidate
            Raises:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
