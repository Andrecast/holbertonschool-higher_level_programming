#!/usr/bin/python3
"""
Read a file and prints it to stdout
"""


def read_file(filename=""):
    """
    Fuction that reads from file
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip())
