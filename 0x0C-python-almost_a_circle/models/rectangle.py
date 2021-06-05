#!/usr/bin/python3
"""
rectangle
"""
 # se debe importar la clase, porq está en otro archivo
from models.base import Base

class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        # llamar el id de la super clase
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """1. width setter, value será el nuevo valor"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """1. height setter, value será el nuevo valor"""
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """1. x setter, value será el nuevo valor"""
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @x.setter
    def y(self, value):
        """1. y setter, value será el nuevo valor"""
        self.__y = value
    