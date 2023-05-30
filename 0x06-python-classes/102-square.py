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
        if not (isinstance(size, int) or isinstance(size, float)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ area: calculates and returns the area of the square."""
        return self.size * self.size

    def __eq__(self, other):
        """defines comparison criteria =="""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """defines comparison criteria !="""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """defines comparison criteria >"""
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """defines comparison criteria >="""
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """defines comparison criteria <"""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """defines comparison criteria <="""
        if isinstance(other, Square):
            return self.area() <= other.area()
