#!/usr/bin/python3
"""Defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representation of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the a Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for square size
            Args:
                value: value to set for size
            Raises:
                TypeError: if value is not an integer
                ValueError: if value <= 0
        """
        self.width = value
        self.height = value

    def __str__(self):
        """returns a custom representation of the square instance"""
        s = "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id, self.x, self.y, self.width
                )
        return s
