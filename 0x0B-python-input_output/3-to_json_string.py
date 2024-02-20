#!/usr/bin/python3
import json

"""This module defines the function to_json_string"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj (Object): The object
    """
    return json.dumps(my_obj)
