#!/usr/bin/python3
"""This module has the add attribute function"""


def add_attribute(obj, attr, value):
    """Function that adds an attribute to an object if it is possible
    """

    if "__dict__" not in dir(type(obj)):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr] = value
