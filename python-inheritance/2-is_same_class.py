#!/usr/bin/python3
"""Function to check in an object is an exact instance of a class"""


def is_same_class(obj, a_class):
    """returns True if obj is an exact instance of a_class"""
    return type(obj) is a_class
