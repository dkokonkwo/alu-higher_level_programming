#!/usr/bin/python3
"""creates object from json file"""


def load_from_json_file(filename):
    "converts json file to python and returns"
    import json
    with open(filename, "r") as f:
        return json.load(f)
