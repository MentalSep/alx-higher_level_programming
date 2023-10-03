#!/usr/bin/python3
""" This module contains text_indentation"""


def text_indentation(text):
    """ This function prints a text with 2 new lines after delimters"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ")
                                      for line in text.split(delim)])
    print(text, end="")
