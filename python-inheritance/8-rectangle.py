#!/usr/bin/python3
"""defines class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiates width and height in the class"""
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.integer_validator(self, "width", self.__width)
        self.integer_validator(self, "height", self.__height)
