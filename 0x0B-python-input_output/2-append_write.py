#!/usr/bin/python3
"""This module contains append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf-8") as text_file:
        return text_file.write(text)
