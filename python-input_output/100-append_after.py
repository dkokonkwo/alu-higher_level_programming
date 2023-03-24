#!/usr/bin/python3
"""Replace an old string with a new one"""


def append_after(filename="", search_string="", new_string=""):
    """reads the file and replaces the string"""
    with open(filename, "r") as f:
        content = f.read()
        content = content.replace(search_string, new_string)
    with open(filename, "w") as f:
        f.write(content)
        f.close()
