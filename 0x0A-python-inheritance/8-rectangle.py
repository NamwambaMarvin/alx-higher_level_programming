#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Rectangle module that inherits from the base class
"""


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from the Base Geometry
    """
    def __init__(self, width, height):
        """
        Initialises variables
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
