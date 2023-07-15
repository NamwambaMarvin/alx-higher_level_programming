#!/usr/bin/python3
"""
Module that stores an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves file to json
    """
    toSave = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(toSave)
