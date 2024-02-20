#!/usr/bin/python3

"""This module contains the definition for the function, read_file"""


def read_file(filename=""):
    """Read a text file and print it to stdout

    Args:
        filename (str): The name of the file to read, empty string by default
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
