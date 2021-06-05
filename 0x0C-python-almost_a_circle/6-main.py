#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

#  x son espacios al inicio de línea
#  y son saltos de línea
if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
