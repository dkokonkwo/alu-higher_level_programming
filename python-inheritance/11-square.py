#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiates and defines area and str methods"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """calulates and returns area of square"""
        return self.__size * self.__size

    def __str__(self) -> str:
        """returns [Square] <size>/<size>"""
        return f"[Square] {self.__size}/{self.__size}"
