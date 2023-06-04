#!/usr/bin/python3
"""say_my_name - contains function that prints out your name"""


def say_my_name(first_name, last_name=""):
    """prints out first_name last_name
        Args:
            first_name: str, first name
            last_name: str, last name
        Raises:
            TypeError: if either name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
