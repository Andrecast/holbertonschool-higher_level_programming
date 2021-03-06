#!/usr/bin/python3
"""
This module has a function that prints a square with the character #
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print('#', end="")
        print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
