#!/usr/bin/python3
"""This module contains save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as text_file:
        return json.dump(my_obj, text_file)
