#!/usr/bin/python3
'''
doc here
'''


class BaseGeometry():
    '''
    raise error
    '''
    def area(self):
        '''
        raise excep
        '''
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        '''
        is int?
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
