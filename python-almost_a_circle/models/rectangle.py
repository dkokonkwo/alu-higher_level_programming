#!/usr/bin/python3
"""defines Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """class for Rectangle instances with p.i.a width,height,x,and y"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """gets private instance attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints the shape of the rectangle"""
        row = ''
        for x in range(self.height):
            for y in range(self.width):
                while len(row) < self.width:
                    row += "#"
            print(row)

    def __str__(self):
        """override __str__ with new string in the format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
            str(self.id), str(self.x), str(self.y),
            str(self.width), str(self.height))
        return (str_rep)
