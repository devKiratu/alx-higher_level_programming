#!/usr/bin/python3
"""Square: This module contains the definition of class Square"""


class Square:
    """ A class defining a square
        Attributes:
            __size: length of the side of the square
            __position: offset for the square from 0,0

        Properties:
            size: getter and setter for __size
            position: getter and setter for __position

        Methods:
            area: calculates the area of the square
            my_print: prints out a square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Parameters:
                size:(optional) length of one side of the square
                position:(optional) offset for the square from 0,0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for __position
            Parameters:
                value: tuple representing the position to set
        """
        if isinstance(value, tuple) and len(value) == 2 and \
            all(isinstance(v, int) for v in value) and \
                all(v >= 0 for v in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ area: calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints out a square using the character #"""
        a, b = self.position
        s = " " * a
        if self.size == 0:
            print()
        for i in range(b):
            print()
        for i in range(self.size):
            print("{}".format(s), end="")
            for j in range(self.size):
                print("#", end="")
            print()
