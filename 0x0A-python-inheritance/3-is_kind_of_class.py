#!/usr/bin/python3
"""
Checks for inheritance
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks for inheritance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
