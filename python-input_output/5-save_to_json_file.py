#!/usr/bin/python3
"""write json rep into a text file"""


import json


def save_to_json_file(my_obj, filename):
    """converts object to json and writes it to a file"""
    y = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(y)
        f.close
