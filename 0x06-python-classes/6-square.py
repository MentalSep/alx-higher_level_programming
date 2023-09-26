#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size, position variables as a private instances"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """This function returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This function sets the position of the square"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """This function prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
