#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    Function that prints a pascal triangle
    """
    rows = []
    for line in range(1, n + 1):
        numbers = []
        C = 1
        for i in range(1, line + 1):
            numbers.append(C)
            C = int(C * (line - i) / i)
        rows.append(numbers)
    return rows
