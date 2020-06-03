#!/usr/bin/python3


"""BaseGeometry Class module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Squeare class
    Args:
        Rectangle (class) : class to inherit
    """

    def __init__(self, size):
        """Inizialition Square Class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        