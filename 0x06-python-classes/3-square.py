#!/usr/bin/python3
"""Defining a class Square."""

class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initialize the new square.
        Args:
            size (int): The size of  new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Use public instance to 
        Return the current area of the square.
        """
        return (self.__size * self.__size)
