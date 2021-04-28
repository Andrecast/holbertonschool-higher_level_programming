#!/usr/bin/env python3
def uppercase(str):
    for s in range(0, len(str)):
        num = ord(str[s])
        if num > 96 and num < 123:
            num = num - 32  # aquí empiezan las mayúsculas
            print(chr(num), end="")
    print()
