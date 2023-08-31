#!/usr/bin/python3
"""Defines a function for finding the peak in a list of integers """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.
        Args:
            list_of_integers: the list for which to fnd a peak
    """
    if not isinstance(list_of_integers, list):
        return None
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    i = 1
    j = len(list_of_integers) - 1

    while i <= j:
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
        if list_of_integers[j] > peak:
            peak = list_of_integers[j]
        i += 1
        j -= 1
    return peak
