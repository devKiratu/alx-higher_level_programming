#!/usr/bin/python3
"""Square: This module contains the definition of class Square"""


class Square:
    """ A class defining a square
        Attributes:
            __size: length of the side of the square

        Properties:
            size: getter and setter for __size

        Methods:
            area: calculates the area of the square
            my_print: prints out a square with the character #
    """
    def __init__(self, size=0):
        """ Parameters:
                size:(optional) length of one side of the square
        """
        self.size = size

    @property
    def size(self):
        """getter for __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter for the attribute __size
            Parameters:
                size: value for initializing  __size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ area: calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints out a square using the character #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
