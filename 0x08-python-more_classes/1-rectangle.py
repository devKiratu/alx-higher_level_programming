#!/usr/bin/python3
"""Rectangle - defines a rectangle"""


class Rectangle:
    """class representation of a rectangle
        Attributes:
            __width: rectangle width
            __height: rectangle height
    """
    def __init__(self, width=0, height=0):
        """__init__ - object constructor
            Args:
                width: optional width of the rectangle
                height: optional height of the rectangle
            Raises:
                TypeError: if width/height is not an integer
                ValueError: if width/height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
            Args:
                value: the new value for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for property height"""
        return self.__height

    @width.setter
    def height(self, value):
        """Setter for height
            Args:
                value: the new value for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value