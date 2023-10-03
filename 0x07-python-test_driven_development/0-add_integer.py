#!/usr/bin/python3
""" This module adds two integers """


def add_integer(a, b=98):
    """ This function adds two integers """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
