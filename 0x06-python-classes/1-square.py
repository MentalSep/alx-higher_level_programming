#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private attribute - size"""
    def __init__(self, size):
        """Initializes the size variable as a private instance"""
        self.__size = size
