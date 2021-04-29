#!/usr/bin/python3
for i in reversed(range(97, 123)):  # otra forma, sin reversed: range(122, 96, -1)
    if i % 2 != 0:  # si es impar, vuelvalo mayuscula
        i = i - 32
    print("{:c}".format(i), end="")
