#!/usr/bin/python3
"""class that defines a rectangle"""

class Rectangle:
    """this class will represent a rectangle"""


    def __init__(self, width=0, height=0):
        """Initialize a rectangle class
        Args:
            width: will represent the width of the rectangle
            height: will represent the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = heigt

    @property
    def width(self):
        """will get width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """will get height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
