#!/usr/bin/python3
"""converts class to json"""


def class_to_json(obj):
    """returns object class dictionary"""
    return obj.__dict__
