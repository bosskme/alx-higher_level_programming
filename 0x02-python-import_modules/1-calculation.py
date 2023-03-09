#!/usr/bin/python3

# Import the required functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define a and b
a = 10
b = 5

# Perform addition and print the result
result_add = add(a, b)
print(f"{a} + {b} = {result_add}")

# Perform subtraction and print the result
result_subtract = subtract(a, b)
print(f"{a} - {b} = {result_subtract}")

# Perform multiplication and print the result
result_multiply = multiply(a, b)
print(f"{a} * {b} = {result_multiply}")

# Perform division and print the result
result_divide = divide(a, b)
print(f"{a} / {b} = {result_divide}")
