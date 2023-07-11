#!/usr/bin/python3
"""
The square module( inherits from Rectangle)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The square class
    """
    def __init__(self, size):
        integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
