#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The initialization method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The str method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The update method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """The to_dictionary method"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
