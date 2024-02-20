#!/usr/bin/python3
import json

"""This module defines the function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation

    Args:
        my_obj (Object): The object we want to write
        filename (str): The name of the file we would like to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
