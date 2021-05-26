#!/usr/bin/python3
"""
This module has a function that
adds 2 integers
Return a + b
"""


def add_integer(a, b=98):
    """
    This function adds two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
