#!/usr/bin/python3
"""
    Rectangle class representation
"""


class Rectangle:
    """
    Rectangle class
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Documentation for the init funtion
        """

        self.check(width, height)
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Detects instance deletion
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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
                rectangle += str(self.print_symbol)
            if i != h - 1:
                rectangle += '\n'
        return rectangle

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles
        """
        ins1 = isinstance(rect_1, Rectangle)
        ins2 = isinstance(rect_2, Rectangle)

        if ins1 is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if ins2 is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        return rect_2

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
