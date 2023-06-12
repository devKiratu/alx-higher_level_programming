#!/usr/bin/python3
"""module for a function that adds a new attribute to an object if
    it’s possible
"""


def add_attribute(obj, attribute, value):
    """adds attribute to obj with value if possible
        Args:
            obj: object to add attribute to
            attribute: attribute to add
            value: value corresponding to attribute
        Raises:
            TypeError: if attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
