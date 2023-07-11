#!/usr/bin/python3
"""
Module to read a file
"""


def read_file(filename=""):
    """
    Function that reads a file
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
