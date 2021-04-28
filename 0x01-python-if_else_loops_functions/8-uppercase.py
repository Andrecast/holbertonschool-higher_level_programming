#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        num = ord(str[i])
        if num > 96 and num < 123:
            num = num - 32  # aquí empiezan las mayúsculas
        print("{:c}".format(num), end="")
    print()
