#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        for k, v in sorted(a_dictionary.items()):
            print("{}: {}".format(k, v))
