#!/usr/bin/python3
"""checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a subclass of a_class
        else False
        Args:
            obj: object to investigate
            a_class: class to check against
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
