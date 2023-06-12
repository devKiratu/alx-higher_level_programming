#!/usr/bin/python3
"""MyList - custom list class that inherits from list"""


class MyList(list):
    """Custom list class"""
    def print_sorted(self):
        """prints sorted list"""
        cp = self[:]
        cp.sort()
        print("{}".format(cp))
