#!/usr/bin/python3
"""defines a function that creates new class attribute"""


def add_attribute(obj, attr, value):
        """creates new attribute if possible"""
        if '__dict__' not in dir(obj):
            raise TypeError("can't add new attribute")
        else:
            setattr(obj, attr, value)
