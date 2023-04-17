#!/usr/bin/python3
"""defines a function that writes a text into a file"""


def write_file(filename="", text=""):
    """overwites a text into file and returns num of characters"""
    with open(filename, "w") as f:
        f.write(text)
        f.close()
    return len(text)
