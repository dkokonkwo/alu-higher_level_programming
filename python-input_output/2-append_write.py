#!/usr/bin/python3
"""Funtion appends text to the end of a text file"""


def append_write(filename="", text=""):
    """appends string at the end of a text file"""
    with open(filename, "a") as f:
        f.write(text)
        f.close()
    return(len(text))
