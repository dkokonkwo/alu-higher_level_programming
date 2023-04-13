#!/usr/bin/python3
"""defines a function that prints text with new lines"""


def text_indentation(text):
    """add 2 new lines when char is . or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_string = ""
    for character in text:
        if character == "." or character == ":":
            new_string += character + "\n\n"
        else:
            new_string += character
    print(new_string.rstrip())
