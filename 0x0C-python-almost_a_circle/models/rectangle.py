#!/usrbin/python3
"""Defines class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width
            Args:
                value: width value
        """
        self.__width = value

    @property
    def height(self):
        """retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height
            Args:
                value: height value
        """
        self.__height = value

    @property
    def x(self):
        """retrieves x offset of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x offset for the rectangle
            Args:
                value: x offset to set
        """
        self.__x = value

    @property
    def y(self):
        """retrieves the y offset of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value for y offset
            Args:
                value: y offset
        """
        self.__y = value
