#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    sum = 0
    for i in range(1, lenght):
        sum = sum + int(argv[i])
    print(sum)
