#!/usr/bin/python3
"""
Checks for inheritance
"""


def inherits_from(obj, a_class):
    """
    Checks for inheritance
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
