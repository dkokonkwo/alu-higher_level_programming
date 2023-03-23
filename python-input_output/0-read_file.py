#!/usr/bin/python3
"""function reads text files and prints it out"""


def read_file(filename=""):
    """read and print out text file"""
    with open(filename) as f:
        print(f.read(), end="")
