#!/usr/bin/python3
import json

"""This module defines the function from_json_string"""


def from_json_string(my_str):
    """Returns a python data structure from a JSON string"""
    return json.loads(my_str)
