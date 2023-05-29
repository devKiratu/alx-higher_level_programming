#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as ex:
        result = None
        print("Exception: {}".format(ex), file=stderr)
    finally:
        return result
