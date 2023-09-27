#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size=0):
        """Initializes the size variable as a private instance"""
        self.__size = size

    def area(self):
        """This function returns the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """This function returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def __eq__(self, other):
        """This function returns True if both objects are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """This function returns True if both objects are different"""
        return self.area() != other.area()

    def __gt__(self, other):
        """This function returns True if self is greater than other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """This function returns True if self is greater than
        or equal to other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """This function returns True if self is less than other"""
        return self.area() < other.area()

    def __le__(self, other):
        """This function returns True if self is less than or equal to other"""
        return self.area() <= other.area()
