#!/usr/bin/python3
"""
Modu;e that adds anew attribute
"""


def add_attribute(obj, attr, value):
    """
    Adds a new atribute
    """
    if obj.attr:
        obj.attr = value
    else:
        raise TypeError('can\'t add new attribute')
