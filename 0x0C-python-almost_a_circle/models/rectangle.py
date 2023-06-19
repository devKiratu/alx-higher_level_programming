#!/usrbin/python3
"""Defines class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle attributes"""
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
            Raises:
                TypeError: if value is not an integer
                ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
            Raises:
                TypeError: if value is not an integer
                ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
            Raises:
                TypeError: if value is not an integer
                ValueError: if value < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
            Raises:
                TypeError: if value is not an integer
                ValueError: if value < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle to stdout using # symbol"""
        if self.y > 0:
            for i in range(self.y):
                print()
        for i in range(self.height):
            if self.x > 0:
                for k in range(self.x):
                    print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns a custom representation of the rectangle"""
        r = "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.width,
                self.height
                )
        return r

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes contained in args, or kwargs when args
            does not exist or is empty
            Args:
                args: new attributes list
                kwargs: a dict of the new attributes
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of the Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
