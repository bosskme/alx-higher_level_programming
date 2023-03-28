#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        # Use slicing to get the first x elements of the list
        elements_to_print = my_list[:x]
        # Loop through the elements and print them on the same line
        for element in elements_to_print:
            print(element, end=' ')
        # Print a new line after all elements have been printed
        print()
        # Return the number of elements that were printed
        return len(elements_to_print)
    except:
        # If an exception occurs, return 0
        return 0
