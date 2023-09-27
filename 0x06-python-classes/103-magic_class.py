#!/usr/bin/python3
"""This module creates a class MagicClass that defines a magic class"""
import math


class MagicClass:
    """MagicClass class with a private instance attribute - radius"""
    def __init__(self, radius=0):
        """Initializes the radius variable as a private instance"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This function returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This function returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
