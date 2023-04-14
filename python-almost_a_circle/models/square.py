#!/usr/bin/python3
"""defines Square class that inherits from Rectangle"""


from models.rectangle import Rectangle



class Square(Rectangle):
    """inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiates public attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets private instance attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets private instance attribute size and
        uses to set width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """override __str__ with new string in the format
        [Square] (<id>) <x>/<y> - <size>"""
        str_rep = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_rep)
