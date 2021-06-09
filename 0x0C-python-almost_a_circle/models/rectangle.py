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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @y.setter
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
        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        x son espacios al inicio de línea
        y son saltos de línea
        """
        print('\n' * self.__y, end="")
        print((" " * self.__x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}\
        ".format(__class__.__name__, self.id, self.__x, self.__y, self.__width,
                 self.__height)

    def update(self, *args, **kwargs):
        if args:
            names = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        dictionary = {"id": self.id, "width": self.width,
                      "height": self.height, "x": self.x,
                      "y": self.y}
        return dictionary
