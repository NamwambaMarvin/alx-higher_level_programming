#!/usr/bin/python3
"""Square Class

A class that defines properties of a square

"""


class Square:
    """__init__

    The __init__ method instantiates the Square class

    Attributes:
        size(:obj`int`:, optional): Square size

    Raises:
        TypeError: if `size` type is not `int`.

        ValueError: if `size` is less than 0

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
