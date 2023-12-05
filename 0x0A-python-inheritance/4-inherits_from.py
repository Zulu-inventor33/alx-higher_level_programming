#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns true when object is an instance of a class that inherited
    (directly or indirectly) from de specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
