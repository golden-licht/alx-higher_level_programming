#!/usr/bin/python3

"""This module defines the function text_indentation"""


def text_indentation(text):
    """Print a text with 2 new lines after each of
    these characters: ., ? and :

    No space at the beginning or at the end of each printed line.

    Args:
        text (str)

    Raises:
        TypeError: If text is not string.
    """
    characters = {'.', '?', ':'}
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in text:
        if x == ' ' and prev is True:
            continue
        prev = False
        print(x, end="")
        if x in characters:
            print("\n")
            prev = True
