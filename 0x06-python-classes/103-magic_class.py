#!/usr/bin/python3
"""MagicClass - computes area and circumference of a circle given radius"""


import math


class MagicClass:
    """MagicClass
        Attributes:
            __radius: radius of a circle
        Methods:
            area: computes area
            circumference: computes circumference
    """

    def __init__(self, radius):
        """__init__
            Parameters:
                radius: radius to assign the circle object
            Raises:
                TypeError: if radius is not a number
        """
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area - computes area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circumference - computes circumference of a circle"""
        return (2 * math.pi * self.__radius)
