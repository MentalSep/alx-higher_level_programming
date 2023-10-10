#!/usr/bin/python3
"""This module contains Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
