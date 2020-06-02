#!/usr/bin/python3

""" Import BaseGeometry Class module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry

    Args:
        BaseGeometry (Class): class to inherit
    """
    def __init__(self, width, height):
        self.integer_validator("widht", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
