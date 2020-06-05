#!/usr/bin/python3
""" Defines a class Base
"""


class Base:
    """Class that manage id attribute in all your future classes
       and to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Assign an id number

        Args:
            id ([int], optional): id number. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
