#!/usr/bin/python3
"""0-add_integer - contains function `add_integer` that adds two integers
    Usage:
        sum = add_integer(5) # the second integer uses the default value, 98
        sum = add_integer(5, 3) # overrides default value for second integer
"""


def add_integer(a, b=98):
    """Returns the sum of a and b

        Args:
            a: first integer
            b: second integer
        Raises:
            TypeError: if either a or b is neither an integer nor a float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
