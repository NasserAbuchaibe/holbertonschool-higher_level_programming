#!/usr/bin/python3
"""module for class BaseGeometry
"""


class BaseGeometry():
    """empty class
    """
    def area(self):
        """ method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
