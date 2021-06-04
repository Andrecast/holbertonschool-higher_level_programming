#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    Function that prints a pascal triangle
    """
    filas = []
    if n <= 0:
        return filas
    if n == 1:
        filas = [[1]]
        return filas
    filas = [[1], [1, 1]]
    for i in range(1, (n - 1)):
        colum = [1]
        for j in range(0, len(filas[i]) - 1):
            colum.extend([filas[i][j] + filas[i][j + 1]])
        colum += [1]
        filas.append(colum)
    return filas
