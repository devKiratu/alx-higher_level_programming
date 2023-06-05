#!/usr/bin/python3
"""contains function that prints a square with the character '#'"""


def print_square(size):
    """prints a square of length 'size'
        Args:
            size: length of side of square to print
        Raises:
            TypeError: - if size is not an integer
                        - if size is a float and less than zero
            ValueError: if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()
