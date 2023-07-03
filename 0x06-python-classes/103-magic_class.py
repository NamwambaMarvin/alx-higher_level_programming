#!/usr/bin/python3
import dis
import math

"""Magic Class module

For comuting byte code

"""


class MagicClass:
    """Magic Class

    This is a magic class

    """

    def __init__(self, radius=0):
        """__init__

        The class constructor

        Attributes:
            raduis(:obj:`int`, optional): Radius of the circle

        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Computes the area of hte circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes the circumference of the circle
        """
        return 2 * math.pi * self.__radius
