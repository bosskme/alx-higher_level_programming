#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contexts of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
