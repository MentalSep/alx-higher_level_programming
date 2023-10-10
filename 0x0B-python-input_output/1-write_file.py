#!/usr/bin/python3
"""This module contains write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written"""
    with open(filename, mode="w", encoding="utf-8") as text_file:
        return text_file.write(text)
