#!/usr/bin/python3
"""Defines a function that prints Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal’s triangle of n
        n: size of Pascal's triangle
    """
    pt = []
    for i in range(1, n+1):
        if i == 1:
            pt.append([1])
        elif i == 2:
            pt.append([1, 1])
        else:
            row = [1]
            prev = pt[-1]
            i = 0
            j = 1
            while j < len(prev):
                row.append(prev[i] + prev[j])
                i += 1
                j += 1
            row.append(1)
            pt.append(row)
    return pt
