#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        wr = file.write(text)
        return wr
