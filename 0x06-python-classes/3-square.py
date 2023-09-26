#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """Initializes the size variable as a private instance"""
        self.__size = size
    def area(self):
        """This function returns the area of the square"""
        return (self.__size * self.__size)
