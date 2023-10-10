#!/usr/bin/python3
"""This module contains read_file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as text:
        print(text.read(), end="")
