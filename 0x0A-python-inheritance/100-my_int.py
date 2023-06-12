#!/usr/bin/python3
"""MyInt - custom class that inherits from int"""


class MyInt(int):
    """MyInt - rebel class that inverts the == and != operators"""
    def __eq__(self, value):
        """returns false if the values are equal and true if not
            Args:
                value: value to compare with
        """
        if type(value) is int:
            return self.real != value

    def __ne__(self, value):
        """returns true if values are equal and false if not
            Args:
                value: value to compare with
        """
        if type(value) is int:
            return self.real == value
