#!/usr/bin/python3
"""
Module to convert json into an object
"""
import json


def from_json_string(my_str):
    """
    Function to convert json into an object
    """
    return json.loads(my_str)
