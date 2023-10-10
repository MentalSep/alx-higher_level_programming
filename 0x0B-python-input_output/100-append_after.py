#!/usr/bin/python3
"""This module contains append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each
    line containing a specific string"""
    with open(filename, mode="r+", encoding="utf-8") as text:
        lines = text.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        text.seek(0)
        text.writelines(new_lines)
