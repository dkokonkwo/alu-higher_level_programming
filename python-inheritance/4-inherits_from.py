#!/usr/bin/python3
"""Function to check in an object is an instance of a class"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class inherited from a specified a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
