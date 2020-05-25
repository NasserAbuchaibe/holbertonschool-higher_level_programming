#!/usr/bin/python3
"""7-rectangle.py: Class Rectagle
"""


class Rectangle:
    """class Rectagle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Sets a height and width
        Args:
            width (int): width rectangle
            height (int): heigth rectagle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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

    def __str__(self):
        """ print the rectangle """
        aux_str = ""
        if self.__width == 0 or self.__height == 0:
            return aux_str
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        for x in range(self.__height):
            if x == self.__height - 1:
                aux_str += self.print_symbol * self.__width
            else:
                aux_str += (self.print_symbol * self.__width) + '\n'
        return aux_str

    def __repr__(self):
        """ returns string for the eval function """
        return 'Rectangle({}, {})'.format(self.__width, self.height)

    def __del__(self):
        """delete the object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (int): rect_1 area
            rect_2 (int): rect_2 area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns the class instance

         Args:
         size (int): new size for width and height, Defaults to 0.
         """
        return Rectangle(size, size)
