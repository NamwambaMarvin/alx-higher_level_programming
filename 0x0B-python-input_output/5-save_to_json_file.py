#!/usr/bin/python3
"""
Module that stores an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves file to json
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
