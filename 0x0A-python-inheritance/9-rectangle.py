#!/usr/bin/python3
"""Rectangle Class, inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class representation for Rectangle"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
