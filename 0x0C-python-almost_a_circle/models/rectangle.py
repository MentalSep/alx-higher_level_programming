#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initialization method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """The height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """The x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """The y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """The area method"""
        return self.__width * self.__height

    def display(self):
        """The display method"""
        string = ""
        for i in range(self.__y):
            string += '\n'
        for i in range(self.__height):
            string += ' ' * self.__x
            string += '#' * self.__width
            string += '\n'
        print(string, end='')

    def __str__(self):
        """The __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """The update method"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """The to_dictionary method"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
