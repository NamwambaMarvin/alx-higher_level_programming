#!/usr/bin/python3
"""
An empty class of BaseGeometry module
"""


class BaseGeometry:
    """
    Empty class of base geometry module
    """
    def area(self):
        """
        Raises an exception about the implementation
        of area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
