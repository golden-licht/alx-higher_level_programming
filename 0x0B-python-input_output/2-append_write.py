#!/usr/bin/python3

"""This module defines the function append_write"""


def append_write(filename="", text=""):
    """Append a text to a file, if file doesn't exist, create it

    Args:
        filename (str): The name of the file to append text to; \\
        Defaults to empty string
        text (str): The text; Defaults to empty string

    Returns:
        int: The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
