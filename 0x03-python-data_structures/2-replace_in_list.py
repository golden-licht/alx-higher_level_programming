#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
        my_list.insert(idx, element)
    return my_list
