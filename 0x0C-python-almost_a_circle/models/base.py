#!/usr/bin/python3
"""This model defines a class Base"""


import json


class Base:
    """Represent a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the base class

        Args:
            id: the id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list dictionaries to json string"""

        if list_dictionaries is None or list_dictionaries\
                == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string to a file"""

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding='utf-8') as f:
            if list_objs is None:
                list_ = []
                string_to_save = Base.to_json_string(list_)
                f.write(string)
            else:
                new_list = []
                for i in list_objs:
                    new_dict = cls.to_dictionary(i)
                    i = new_dict
                    new_list.append(i)
                string = Base.to_json_string(new_list)
                f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Returns list from json string"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            new_instance = cls(4, 5)
            new_instance.update(**dictionary)
            return new_instance
        if cls.__name__ == "Square":
            new_instance = cls(4)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances loaded from a file"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding='utf-8') as f:
                json_string = f.read()

                list_of_instances = cls.from_json_string(json_string)

                new_list_of_instances = []

                for i in list_of_instances:
                    new_instance = cls.create(**i)
                    new_list_of_instances.append(new_instance)

                return new_list_of_instances

        except FileNotFoundError:
            return []
