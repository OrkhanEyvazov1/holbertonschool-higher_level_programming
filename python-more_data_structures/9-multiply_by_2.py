#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for a in a_dictionary.keys():
        a_dictionary[a] = a_dictionary[a]*2
    return a_dictionary
