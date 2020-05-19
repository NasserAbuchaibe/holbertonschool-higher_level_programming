#!/usr/bin/python3

"""2-square.py: Class Square"""


class Square:
    """Class  Square: initialize the size attribute """
    def __init__(self, size=0):
        """
        initialize the square class with size
        Args:
        size: size of square
        Return:
        None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """ Calculate and return the area of the square """
        return self._Square__size ** 2
