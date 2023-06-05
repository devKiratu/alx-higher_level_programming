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
        self.height = height
        self.width = width

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
            Args:
                value: the new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area: returns area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter: calculates the perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """return a string representation of the rectangle"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for r in range(self.height):
            row = ""
            for c in range(self.width):
                row += '#'
            if r != self.height - 1:
                row += "\n"
            rect += row
        return rect

    def __repr__(self):
        """return string representation of a rectangle object that can be
            used to recreate a new instance using eval()
        """
        return f"Rectangle({self.width}, {self.height})"
