#!/usr/bin/python3
"""
Module that contains the class MyList
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
