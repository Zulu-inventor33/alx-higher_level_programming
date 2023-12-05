#!/usr/bin/python3
"""an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object's available attribtes."""
    return (dir(obj))
