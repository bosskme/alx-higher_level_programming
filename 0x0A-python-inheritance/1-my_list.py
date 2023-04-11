#!/usr/bin/python3

"""Defines an inherited list class MyList."""


Class MyList(list):
    """Here we implement sorted printing for the 
built-in list class."""


    def print_sorted(self):
        """Here we print a list in sorted ascending order."""


        print(sorted(self))
