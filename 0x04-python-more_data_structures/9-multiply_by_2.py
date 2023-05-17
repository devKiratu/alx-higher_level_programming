#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        new_ls = map(lambda kvp: (kvp[0], kvp[1] * 2), a_dictionary.items())
        return dict(new_ls)
