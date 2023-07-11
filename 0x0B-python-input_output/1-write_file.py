#!/usr/bin/python3
"""
Module that counts number of lines
"""


def number_of_lines(filename=""):
    """
    Functio to count the numver of lines
    """
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
