#!/usr/bin/python3
"""creates student class with public instance attributes"""


class Student:
    """initializes instance attributes"""
    def __init__(self, first_name, last_name, age) -> None:
        """public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """returns attr if in self.__dict else returns self.__dict__"""
        if type(attrs) is list:
            n_dict = {}
            for key in self.__dict__:
                for i in attrs:
                    if i == key:
                        n_dict[i] = self.__dict__[i]
            return n_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace value of attributes"""
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            if key == "last_name":
                self.last_name = json[key]
            if key == "age":
                self.age = json[key]
