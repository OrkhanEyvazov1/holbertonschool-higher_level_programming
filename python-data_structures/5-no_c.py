#!/usr/bin/python3

def no_c(my_string):
    return ''.join(map(
        lambda x: '' if x == 'C' or x == 'c' else x, my_string
    ))
