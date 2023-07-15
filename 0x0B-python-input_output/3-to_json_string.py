#!/usr/bin/python3
"""
Module that converts JSON to a string
"""
import json


def to_json_string(my_obj):
    """
    Converts an object to a string
    """
    return json.dumps(my_obj)
