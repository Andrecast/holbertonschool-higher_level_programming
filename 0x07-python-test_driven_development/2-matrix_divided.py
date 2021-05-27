#!/usr/bin/python3
"""
This module has a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    """

    # div quality checking
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    standard_length = 0
    div_matrix = []

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if isinstance(matrix[0], list):
            standard_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(row) != standard_length:
            raise TypeError("Each row of the matrix must have the same size")
        div_row = []
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            div_row.append(round(element/div, 2))
        div_matrix.append(div_row)
    return div_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
