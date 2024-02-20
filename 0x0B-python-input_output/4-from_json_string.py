#!/usr/bin/python3

"""This module defines the function from_json_string"""
import json


def from_json_string(my_str):
    """Returns a python data structure from a JSON string"""
    return json.loads(my_str)
