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
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
