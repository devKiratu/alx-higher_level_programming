#!/usr/bin/python3
"""Square Class, inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class representation for Square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = super().integer_validator("size", size)

    def area(self):
        """returns area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """returns string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
