#!/usr/bin/python3
"""
Custom list module
"""


class MyList(list):
    """
    MyList Class extends list class in the py lib
    """
    def __init__(self, iterable):
        super().__init__(int(item) for item in iterable)

    """
    print sorted - Prints a list i sorted order
    """
    def print_sorted(self):
        print(super().sort(item))
