#!/usr/bin/python3
"""
Module that creates a json object from a file
"""
from json import loads


def load_from_json_file(filename):
    """
    Load a json object from a file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return loads(f.read())
