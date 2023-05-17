#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        keys = []
        for k, v in a_dictionary.items():
            if v == value:
                keys.append(k)
        for i in keys:
            del a_dictionary[i]
    return a_dictionary
