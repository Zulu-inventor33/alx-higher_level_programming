#!/usr/bin/python3
"""A module that defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
