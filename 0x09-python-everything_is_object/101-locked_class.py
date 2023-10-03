#!/usr/bin/python3
"""This module creates a class that has restrictions"""


class LockedClass:
    """This class has restrictions on what attributes can be set"""
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """Initializes an instance of the class"""
        self.first_name = first_name
