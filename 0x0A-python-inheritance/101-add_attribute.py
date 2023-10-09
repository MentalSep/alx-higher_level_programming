#!/usr/bin/python3
"""Module that contains add_attribute function"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it’s possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
