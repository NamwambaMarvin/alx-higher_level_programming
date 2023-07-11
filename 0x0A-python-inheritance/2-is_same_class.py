#!/usr/bin/python3
"""
Checks instances of objects
"""


def is_same_class(obj, a_class):
    """
    Checks instances of objects
    """
    if type(obj) == a_class:
        return True
    else:
        return False
