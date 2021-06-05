#!/usr/bin/python3
"""
Class Base
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        """
        if id:  # si el usuario pasa un id, lo asigna
            self.id = id
        else:  # si no pasa un id, se asigna el del contador
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
