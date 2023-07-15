#!/usr/bin/python3
"""
Module that appends to  a file
"""


def append_write(filename="", text=""):
    """
    Function that appends to a file
    """
    with open(filename, 'a') as f:
        return f.write(text)
