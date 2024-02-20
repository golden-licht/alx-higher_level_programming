#!/usr/bin/python3

"""This module contains the definition for the function write_file"""


def write_file(filename="", text=""):
    """Write a text to a file, if file doesn't exist, create it

    Args:
        filename (str): The name of the file to write text to; \\
        Defaults to empty string
        text (str): The text; Defaults to empty string

    Returns:
        int: The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
