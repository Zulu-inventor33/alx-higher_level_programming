#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for j in a_dictionary:
            if j == key:
                a_dictionary[j] = value
    return a_dictionary
