#!/usr/bin/python3
"""defines a function that return json string to python"""


import json


def from_json_string(my_str):
    """converts json string to python"""
    y = json.loads(my_str)
    return y
