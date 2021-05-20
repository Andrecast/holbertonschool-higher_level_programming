#!/usr/bin/python3
""" Current square area """


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        for t in value:
            if type(t) is not int or len(value) != 2\
                 or t < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size != 0:
            if self.__position[1] > 0:
                for i in range(0, self.__position[1]):
                    print("")
            for x in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
