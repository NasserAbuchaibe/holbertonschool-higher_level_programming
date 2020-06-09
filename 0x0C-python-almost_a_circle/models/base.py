#!/usr/bin/python3
""" Defines a class Base
"""


import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the CSV string representation of list_objs to a file
        """
        file_csv = cls.__name__ + ".csv"
        with open(file_csv, 'w', newline='') as f:
            csv_f = csv.writer(f)
            if cls.__name__ is "Rectangle":
                for o in list_objs:
                    csv_f.writerow([o.id, o.width, o.height,
                                    o.x, o.y])
            elif cls.__name__ is "Square":
                for o in list_objs:
                    csv_f.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        file_csv = cls.__name__ + ".csv"
        fl = []
        try:
            with open(file_csv, 'r') as f:
                csv_r = csv.reader(f)
                for field in csv_r:
                    if cls.__name__ is "Rectangle":
                        dict1 = {"id": int(field[0]),
                                 "width": int(field[1]),
                                 "height": int(field[2]),
                                 "x": int(field[3]),
                                 "y": int(field[4])}
                    elif cls.__name__ is "Square":
                        dict1 = {"id": int(field[0]), "size": int(field[1]),
                                 "x": int(field[2]), "y": int(field[3])}
                    obj = cls.create(**dict1)
                    fl.append(obj)
        except:
            pass
        return fl
