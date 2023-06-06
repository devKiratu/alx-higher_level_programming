#!/usr/bin/python3
"""Locked class, prevents dynamic creation of new instance attributes
    except if the new instance attribute is called first_name
"""


class LockedClass:
    """LockedClass - prevents dynamic creation of instance attributes
        apart from first_name
    """
    __slots__ = ['first_name']
