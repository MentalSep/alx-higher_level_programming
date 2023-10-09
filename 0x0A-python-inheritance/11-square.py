#!/usr/bin/python3
"""Module that contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size):
        """Instantiation of Square class with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
