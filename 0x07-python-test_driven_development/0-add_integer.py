#!/usr/bin/python3
"""
    Python module to add two integers
"""


def add_integer(a, b=98):
    """add_integer
    Adds two integers a and b
    """
    if type(a) not in (int float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
