#!/usr/bin/python3
import json


"""functions convert python to json"""


def to_json_string(my_obj):
    """converts python object to json rep"""
    y =  json.dumps(my_obj)
    return y
