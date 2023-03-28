#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        # If no exception occurred, return True
        return True
    except:
        # If an exception occurred, return False
        return False
