#!/usr/bin/python3
"""
Module that counts number of lines
"""


def write_file(filename="", text=""):
    """
    Writes text to a file
    """
    with open(filename, 'w') as f:
        f.write(text)
        f.close()
