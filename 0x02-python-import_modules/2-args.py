#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    if lenght == 1:
        print("{} {}".format((lenght - 1), "arguments."))
    elif lenght == 2:
        print("{} {}".format((lenght - 1), "argument:"))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} {}".format((lenght - 1), "arguments:"))
        for i in range(1, lenght):
            print("{}: {}".format(i, argv[i]))
