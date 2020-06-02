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

        Arguments:
            name (str): name
            value (int) number int > 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
