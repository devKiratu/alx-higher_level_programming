#!/usr/bin/python3
"""Divide Matrix - this module contains a function that divides all elements
    of a matrix
"""


def matrix_divided(matrix, div):
    """matrix_divided: divides all elements of a matrix b div
        Args:
            matrix: input matrix
            div: divisor
        Raises:
            TypeError: if:
                        - the matrix is not a list of lists of integers/floats
                        - matrix rows are unequal in size
                        - div is not a number
            ZeroDivisionError: if div is zero
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) and
            all(isinstance(el, list) for el in matrix)):
        raise TypeError(matrix_error)
    for r in matrix:
        for el in r:
            if type(el) not in (int, float):
                raise TypeError(matrix_error)
    if len(matrix) > 0:
        length = len(matrix[0])
        if not all(len(r) == length for r in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # perform the division
    output = []
    for r in matrix:
        row = []
        for el in r:
            row.append(float("{:.2f}".format(el/div)))
        output.append(row)
    return output
