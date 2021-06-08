#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}"\
            .format(__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width 

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        public method that assigns attributes
        """
        if args:
            names = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        dictionary = {"id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y}
        return dictionary
