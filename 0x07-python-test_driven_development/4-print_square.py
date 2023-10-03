#!/usr/bin/python3
""" This module prints a square with the character # """


def print_square(size):
    """ This function prints a square with the character # """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
