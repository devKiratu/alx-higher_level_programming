#!/usr/bin/python3
"""checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of or a subclass of an instance
        of a_class
        Args:
            obj: the object to check
            a_clas: the class to check against
    """
    return isinstance(obj, a_class)
