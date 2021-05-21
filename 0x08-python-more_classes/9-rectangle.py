#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialized a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width attribute"""
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """Getter for __height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height attribute"""
        self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect
        for row in range(self.height):
            rect += (str(self.print_symbol) * self.width)
            if row != self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                rect_return = rect_2
            else:
                rect_return = rect_1
        return rect_return
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
