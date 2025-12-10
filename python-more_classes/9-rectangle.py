#!/usr/bin/python3
''' doc '''


class Rectangle:
    ''' def req '''
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Calc req area '''
        return self.__width * self.__height

    def perimeter(self):
        ''' calc perimetr of req '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' str representation with # '''
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for _ in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        '''repr'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        ''' handles deletion '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        ''' return rectangle that has bigger area if same area
        returns rect_1 . Both must be instance of Rectangle otherwise
        gives typeerror'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''returns new square rectangle'''
        return cls(size, size)
