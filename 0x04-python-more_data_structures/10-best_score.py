#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and a_dictionary:
        key, val = list(a_dictionary.items())[0]
        for k, v in a_dictionary.items():
            if v > val:
                val = v
                key = k
        return key
    return None
