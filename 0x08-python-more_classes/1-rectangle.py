#!/usr/bin/python3
"""1-rectangle.py: Class Rectagle
"""


class Rectangle:
    """class Rectagle
    """

    def __init__(self, width, height):
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
        return = self.__width

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
