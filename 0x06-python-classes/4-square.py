#!/usr/bin/python3
"""Square

The square module

"""


class Square:
    """Square Class

    New class of a square

    """
    def __init__(self, size=0):
        """__init__

        The __init__ insitiates the class

        Attributes:
            size(:obj:`obj`, optional): The size of the square

        Raises:
            TypeError: If the `size` is not `int`

            ValueError: If the `size` is < 0
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2
