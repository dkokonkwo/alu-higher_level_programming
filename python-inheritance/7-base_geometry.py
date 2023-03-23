#!/usr/bin/python3
"""creates class BaseGeometry and defines its methods"""


class BaseGeometry():
    """methods of BaseGeometry"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
