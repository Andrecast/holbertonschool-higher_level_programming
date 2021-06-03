#!/usr/bin/python3
"""
class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionary representation of a Student instance
        """
        return vars(self)
