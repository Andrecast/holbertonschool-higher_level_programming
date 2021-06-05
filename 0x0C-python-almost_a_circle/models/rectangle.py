#!/usr/bin/python3
"""
rectangle
"""
#  se debe importar la clase, porq está en otro archivo
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
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
        """
        1. width setter, value será el nuevo valor
        2. validation of all setter methods and instantiation
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        1. width setter, value será el nuevo valor
        2. validation of all setter methods and instantiation
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        1. width setter, value será el nuevo valor
        2. validation of all setter methods and instantiation
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @x.setter
    def y(self, value):
        """
        1. width setter, value será el nuevo valor
        2. validation of all setter methods and instantiation
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that returns the rectangle area"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rectangle = ""
        for i in range(self.height):
            rectangle = ('#' * self.width)
            print (rectangle)
