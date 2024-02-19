#!/usr/bin/python3

"""This module contains the definition of the function, MyList"""


class MyList(list):
    """A class which inherits the `list` class"""
    def print_sorted(self):
        """Sorts and prints an integer list"""
        self.sort()
        print(self)
