#!/usr/bin/python3
""" Defines a class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle

        Args:
            width (int): width rectangle
            height (int): heigth rectangle
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id (int, optional): id. Defaults to None.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate rectangle area

        Returns:
            [int]: Area rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ print a rectangle
        """
        for y in range(self.__y):
            print()
        for x in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Returns formatted information display
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:
        """
        my_dict = {}
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['id'] = self.id
        my_dict['height'] = self.height
        my_dict['width'] = self.width
        return my_dict
