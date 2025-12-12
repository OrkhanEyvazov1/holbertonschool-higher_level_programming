#!/usr/bin/python3
'''
doc here
'''


class BaseGeometry:
    '''
    raise error
    '''
    def area(self):
        '''
        raise excep
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        is int?
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    '''
    inherit from Basegeometry, rectangle
    '''
    def __init__(self, width, height):
        '''
        innnit
        '''
        self.integer_validator("width", width)
        self.integer_validator("height",height)
        self.__width = width
        self.__height = height
