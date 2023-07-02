#!/usr/bin/python3
"""Square module

This is the square module

"""


class Square:
    def __init__(self, size=0):
        """__init__
        Instatiates the square class
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the size
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        for idx in range(1, self.area() + 1):
            print('#', end='')
            if idx % self.__size == 0 and idx > 0:
                print()
