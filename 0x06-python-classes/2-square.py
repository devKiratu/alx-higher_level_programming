#!/usr/bin/python3
"""Square: This module contains the definition of class Square"""


class Square:
    """ A class defining a square
        Attributes:
            __size: length of the side of the square
        Methods:
            __set_size: validates argument size and initializes __size
    """
    def __init__(self, size=0):
        """ Parameters:
                size:(optional) length of one side of the square
        """
        self.__set_size(size)

    def __set_size(self, size):
        """ Initializes the attribute __size
            Parameters:
                size: value for initializing  __size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
