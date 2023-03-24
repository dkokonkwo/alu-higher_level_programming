#!/usr/bin/python3
"""Replace an old string with a new one"""


def append_after(filename="", search_string="", new_string=""):
    """reads the file and replaces the string"""
    new_txt = ''
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            new_line = line.replace(search_string, new_string)
            new_txt = new_txt + new_line + "\n"

    f.close()
    with open(filename, "w") as f:
        f.write(new_txt)
        f.close()
