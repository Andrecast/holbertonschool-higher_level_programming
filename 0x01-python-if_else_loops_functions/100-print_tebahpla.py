#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 != 0:  # si es impar, vuelvalo mayuscula
        i = i - 32
    print("{:c}".format(i), end="")
