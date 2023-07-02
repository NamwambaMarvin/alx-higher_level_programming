#!/usr/bin/python3
""" The Square Class

The class defines dimesions of a square

"""


class Square:
    def __init__(self, size=0):
        """__init__

        __init__ It instatiates the sqaure class

        Attributes:
            size(:obj:`int`, optional): The size of the square
        Raises:
            TypeError: If `size` is not `int`

            ValueError: If `size` is less than 0

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """area

        Returns the area of the square

        """
        return self.__size ** 2
