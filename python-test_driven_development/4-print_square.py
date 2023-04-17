#!/usr/bin/python3
"""defines a function that prints square with #"""


def print_square(size):
    """print square of <size> if int and >= 0"""
    row = ''
    error_msg = "size must be an integer"
    if type(size) is not int:
        raise TypeError(error_msg)
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError(error_msg)
    for x in range(size):
        for y in range(size):
            while len(row) < size:
                row += "#"
        print(row)
