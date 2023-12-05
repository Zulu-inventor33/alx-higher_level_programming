#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Returns true if object is an instance of de
    class, otherwise return false
    """
    return (type(obj) == a_class)
