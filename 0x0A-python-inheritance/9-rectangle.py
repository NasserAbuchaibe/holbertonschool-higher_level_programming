#!/usr/bin/python3

""" Import BaseGeometry Class module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry

    Args:
        BaseGeometry (Class): class to inherit
    """
    def __init__(self, width, height):
        """

        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that calculates area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
