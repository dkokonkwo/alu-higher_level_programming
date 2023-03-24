#!/usr/bin/python3
"""creates student class with public instance attributes"""


class Student:
    """initializes instance attributes"""
    def __init__(self, first_name, last_name, age) -> None:
        """public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self) -> dict:
        """returns object attributes dictionary"""
        return self.__dict__
