#!/usr/bin/python3
"""
Custom list module
"""


class MyList(list):
    """
    print sorted - Prints a list i sorted order
    """
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
