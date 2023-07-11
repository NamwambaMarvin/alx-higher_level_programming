#!/usr/bin/python3
"""
Checks for inheritance
"""


def inherits_from(obj, a_class):
    """
    Checks for inheritance
    """
    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
        return True
    else:
        return False
