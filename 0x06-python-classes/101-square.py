#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size, position variables as a private instances"""
        self.size = size
        self.position = position

    def area(self):
        """This function returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This function sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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

    def __str__(self):
        """returns a string representation of the square"""
        if self.__size == 0:
            return ""
        squareStr = ""
        for i in range(self.position[1]):
            squareStr += '\n'
        sqaure_line = '#' * self.__size
        offset_spaces = ' ' * self.__position[0]
        squareStr += offset_spaces + sqaure_line
        for i in range(1, self.__size):
            squareStr += '\n' + offset_spaces + sqaure_line
        return squareStr
