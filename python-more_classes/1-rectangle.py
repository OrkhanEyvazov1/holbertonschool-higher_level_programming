#!/usr/bin/python3
'''
doc here
'''


class Rectangle:
    '''Defy square. '''

    def __init__(self, width=0,height=0):
        '''Init square'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''ret width of reqtangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width of reqtangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        '''ret height of reqtangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height of reqtangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
