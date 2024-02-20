#!/usr/bin/python3

"""This module defines the function add_item"""
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def add_item():
    """Add all command line arguments to a Python list,
    and then save them to a file, file_name"""
    file_name = "add_item.json"

    with open(file_name, mode="a+") as f:
        # since it's opened in append mode, f's position is not 0 if the
        # file is not empty. So we need to set it to 0
        f.seek(0)
        if f.read() == "":
            list_object = []
        else:
            list_object = load_from_json_file(file_name)

    for argument in sys.argv[1:]:
        list_object.append(argument)

    save_to_json_file(list_object, file_name)


if __name__ == "__main__":
    add_item()
