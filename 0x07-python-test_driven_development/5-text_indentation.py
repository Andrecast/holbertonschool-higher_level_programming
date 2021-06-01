#!/usr/bin/python3
"""
This module has a function that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    new = "/n".join(i.strip() for i in text.split("\n"))

    print(new, end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
