#!/usr/bin/python3
"""Defines an addition function"""


def add_integer(a, b=98):
    """returns the sum of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
