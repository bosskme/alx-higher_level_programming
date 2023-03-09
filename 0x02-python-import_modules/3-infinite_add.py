#!/usr/bin/python3
import sys

# Get the arguments
args = sys.argv[1:]

# Initialize the sum to zero
total_sum = 0

# Add each argument to the sum
for arg in args:
    total_sum += int(arg)

# Print the result
print(total_sum)
