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

    def to_json(self, attrs=None):
        """
        return a dictionary representation of a Student instance
        """
        dictionary = {}
        if type(attrs) is list:
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__
        
    def reload_from_json(self, json):
        """
        Public method that replaces
        all attributes of the Student instance
        """
        for i, j in json.items():
            setattr(self, i, j)
