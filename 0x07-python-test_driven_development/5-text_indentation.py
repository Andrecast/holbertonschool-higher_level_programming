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
    characters = ['.', '?', ':']

    position = 0
    for i in text:
        if i in characters:
            if text[position + 1] == " ":
                text = text[:position + 1] + text[position + 2:]
        else:
            position += 1

    position = 0
    for i in text:
        if i in characters:
            text = text[:position + 1] + '\n\n' + text[position + 1:]
            position += 3
        else:
            position += 1

    print(text, end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
