#!/usr/bin/python3
"""
Custom list module
"""


class MyList(list):
    """
    MyList Class extends list class in the py lib
    """
    def __init__(self):
        super().__init__()

    """
    print sorted - Prints a list i sorted order
    """
    def print_sorted(self):
        print(sorted(self))
