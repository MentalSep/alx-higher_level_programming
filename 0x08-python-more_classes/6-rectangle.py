#!/usr/bin/python3
"""This module creates a class Rectangle that defines a rectangle."""


class Rectangle:
    """class Rectangle definition."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(self.height):
            string += "#" * self.width
            if i < self.height - 1:
                string += "\n"

        return string

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
