#!/usr/bin/python3
"""
    Rectangle class representation
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
            Documentation for the init funtion
        """

        self.check(width, height)
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width
        """
        self.__width = value

    @property
    def height(self):
        """
            Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            The height setter
        """
        self.__height = value

    def check(self, width, height):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('height must be >= 0')
        elif height < 0:
            raise ValueError('width must be >= 0')
