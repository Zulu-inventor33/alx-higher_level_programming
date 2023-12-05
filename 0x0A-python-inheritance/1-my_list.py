#!/usr/bin/python3
"""module that inherits from de list class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
