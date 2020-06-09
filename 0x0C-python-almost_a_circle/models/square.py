#!/usr/bin/python3
""" Define Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        """ Initializes the Square

        Args:
            size ([int): size of square
            x (int, optional): coordinate x. Defaults to 0.
            y (int, optional): coordinate y. Defaults to 0.
            id ([int], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted information display
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            pass

    def to_dictionary(self):
        """ returns the dictionary representation of a Square
        """
        my_dict = {}
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        return my_dict
