#!/usr/bin/python3
"""square module"""


class Square:
    """defining a square"""

    def __init__(self, size=0):
        """ a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propey o size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Getting the area of a Square
        Return: The size squared
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
