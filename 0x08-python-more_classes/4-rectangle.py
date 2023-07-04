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
            raise ValueError('width must be >= 0')
        elif height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """
        Calculates the area
        """
        return self.__height * self.width

    def perimeter(self):
        """
        Calculates the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return self.__height * 2 + self.__width * 2

    def __Drect(self):
        """

        Draws a rectangle on the screen

        """
        w = self.__width
        h = self.__height
        rectangle = ''
        if w == 0 or h == 0:
            return rectangle
        for i in range(h):
            for j in range(w):
                rectangle += '#'
            if i != h - 1:
                rectangle += '\n'
        return rectangle

    def __str__(self):
        """
        Rectangle representation
        """
        return self.__Drect()
    def __repr__(self):
        """
        Return a string representation of a rectangle
        """
        wid = str(eval('self.width'))
        h = str(eval('self.height'))
        return 'Rectangle(' + wid + ',' + h + ')'
