#!/usr/bin/python3
import json

"""This module defines the function load_from_json_file"""


def load_from_json_file(filename):
    """Create and return an object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        new_obj = json.load(f)
        return new_obj
