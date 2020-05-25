#!/usr/bin/python3
"""2-rectangle.py: Rectagle Class
"""


class Rectangle:
    """class Rectagle
    """

    def __init__(self, width=0, height=0):
        """ Sets a height and width
        Args:
            width (int): width rectangle
            height (int): heigth rectagle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """set width rectagle
        Args:
            value (int): width rectagle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns heigth """
        return self.__height

    @height.setter
    def height(self, value):
        """set heigth rectagle
        Args:
            value (int): heigth rectagle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate the area of ​​a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of ​​a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
