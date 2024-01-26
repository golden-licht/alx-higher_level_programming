#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = 0
    best_key = None

    for k in a_dictionary:
        if (a_dictionary[k] > best_score):
            best_key = k
            best_score = a_dictionary[best_key]
    return best_key
