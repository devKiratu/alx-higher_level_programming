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

    def update(self, *args, **kwargs):
        """Updates Square attributes contained in args, or kwargs when args
            does not exist or is empty
            Args:
                args: new attributes list
                kwargs: a dict of the new attributes
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
