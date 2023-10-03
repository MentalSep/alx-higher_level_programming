#!/usr/bin/python3
""" This module prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ This function prints My name is <first name> <last name> """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
