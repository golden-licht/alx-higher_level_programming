#!/usr/bin/python3

"""This module contains definition for the class, `Base`"""
import json


class Base:
    """A class to be used as 'base' for other derived classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a `Base` object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list representation of a JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"Return an instance with all attributes already set"""
        # dummy instance
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file.

        Args:
            cls (class): A subclass of Base class.
            list_objs (list): List of instances of cls.
        """
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def load_from_file(cls):
        """Return list of instances from a file containing JSON string
        representation of the attribute: value pairs of the instances"""
        try:
            with open(f'{cls.__name__}.json', 'r', encoding='utf-8') as f:
                list_of_dictionary = cls.from_json_string(f.read())
                list_of_instances = []

                for dictionary in list_of_dictionary:
                    obj = cls.create(**dictionary)
                    list_of_instances.append(obj)
            return list_of_instances
        except FileNotFoundError:
            return []
