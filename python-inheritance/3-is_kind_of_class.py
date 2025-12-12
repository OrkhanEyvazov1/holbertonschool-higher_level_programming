#!/usr/bin/python3
'''
doc here
'''


def is_kind_of_class(obj, a_class):
    '''
    return true if obj is instance of class or it's subclasses
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
