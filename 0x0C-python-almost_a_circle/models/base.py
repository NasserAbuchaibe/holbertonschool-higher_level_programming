#!/usr/bin/python3
""" Defines a class Base
"""


import json


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
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation
            of list_dictionaries
        """
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        """
        fl = []
        file_n = cls.__name__ + ".json"
        if list_objs is not None:
            for x in list_objs:
                fl.append(cls.to_dictionary(x))
        with open(file_n, 'w') as f:
            f.write(cls.to_json_string(fl))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string
        """
        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(5)
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        """
        fl = []
        file_n = cls.__name__ + ".json"
        try:
            with open(file_n, 'r') as f:
                fl = cls.from_json_string(f.read())
            for idx, val in enumerate(fl):
                fl[idx] = cls.create(**val)
        except:
            pass
        return fl
