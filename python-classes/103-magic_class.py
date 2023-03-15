#!/usr/bin/python
"""create a class MagicClass"""


import math

class MagicClass:
    def __init__(self, radius=0) -> None:
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * (math.pi))
    
    def circumfrence(self):
        return (2 * (math.pi) * self.__radius)
