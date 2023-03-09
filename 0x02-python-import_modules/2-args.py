#!/usr/bin/python3
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
if num_args == 1:
    print("1 argument:")
else:
    print(f"{num_args} arguments:")

# Print the list of arguments
if num_args > 0:
    for i in range(num_args):
        print(f"{i+1}: {sys.argv[i+1]}")
else:
    print(".")
