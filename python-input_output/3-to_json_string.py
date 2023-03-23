#!/usr/bin/python3
"""functions convert python to json"""


import json


def to_json_string(my_obj):
    """converts python object to json rep"""
    y =  json.dumps(my_obj)
    return y
