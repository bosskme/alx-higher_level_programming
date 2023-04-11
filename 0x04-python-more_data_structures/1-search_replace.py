#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # create a new list to hold the result
    result = []
    # iterate over each element of the input list
    for element in my_list:
        # if the element matches the search value, add the value to th list
        if element == search:
            result.append(replace)
        else:
            # otherwise, add the original element to the result list
            result.append(element)
            # return the resulting list
            return result
