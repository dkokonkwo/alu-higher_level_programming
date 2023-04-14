#!/usr/bin/python3
"""creates class Base and defines methods"""


class Base:
    """manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiates id and equates to nb_objects if none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list of dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
