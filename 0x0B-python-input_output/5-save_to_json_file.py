#!/usr/bin/python3
"""
Module that stores an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    toSave = json.loads(my_obj)
    with open(filename, 'w') as f:
        f.write(toSave)
