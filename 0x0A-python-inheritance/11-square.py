#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle class"""

    def __init__(self, size):
        """Init method of Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the square area"""
        return self.__size ** 2

    def __str__(self):
        """String method for Square"""
        return "[Square] {0}/{0}".format(self.__size)
