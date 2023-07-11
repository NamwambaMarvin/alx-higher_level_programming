#!/usr/bin/python3
"""
The square module( inherits from Rectangle)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The square class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area
        """
        return self.__size * self.__size

    def __str__(self):
        return '[Square] ' + str(self.__width) + '/' + str(self.__height)
