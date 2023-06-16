#!/usr/bin/python3
"""Defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representation of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a custom representation of the square instance"""
        s = "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id, self.x, self.y, self.width
                )
        return s
