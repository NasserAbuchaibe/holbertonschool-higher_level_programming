#!/usr/bin/python3

"""6-square.py: Class Square"""


class Square:
    """Class  Square: initialize the size attribute """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize the square class with size
        Args:
        size: size of square
        position: Coordinates in a square
        Return:
        None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif len(position) != 2 or type(position[0]) != int or
        type(position[1]) != int or (position[0] or position[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__size = size
            self.__position = position

    @property
    def size(self):
        """ return size of square """
        return self._Square__size

    @property
    def position(self):
        """ return position on the square """
        return self.__position

    @size.setter
    def size(self, value):
        """ set size square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @position.setter
    def position(self, value):
        """ set position on the square ""
        

    def area(self):
        """ Calculate and return the area of the square """
        return self._Square__size ** 2

    def my_print(self):
        """ print a square """
        size = self._Square__size
        if size == 0:
            print()
        else:
            for i in range(size):
                print("#" * size)
