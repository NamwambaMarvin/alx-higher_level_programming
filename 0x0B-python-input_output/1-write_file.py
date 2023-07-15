#!/usr/bin/python3
"""
Module that counts number of lines
"""


def write_file(filename="", text=""):
    """
    Writes text to a file
    """
    with open(filename, encoding='utf-8') as f:
        f.write(text)
        f.close()
