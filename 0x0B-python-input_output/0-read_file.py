#!/usr/bin/python3
"""A module that will read a file and
and print its contents to stdio"""


def read_file(filename=""):
    """A function that will take the input"""
    with open(filename,"r") as f:
        """printing the content"""
        print(f.read())
