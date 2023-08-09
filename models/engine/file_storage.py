#!/usr/bin/python3

"""
get json model
"""

import json
from os import path

"""
file storage class
"""


class FileStorage():

    """
    initiate the class
    """
    __file_path = 'file.json'
    __objects = {}

    """
    returns the dictionary __objects
    """
    def all(self):
        return self.__objects

    """
    sets in __objects the obj with
    key <obj class name>.id
    """
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    """
    Serializes __objects to the
    JSON file (path: __file_path)
    """
    def save(self):
        my_dict = {}
        """Loop and convert object to dict"""
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        """ open file in file path __file_path and save the dict """
        with open(self.__file_path, mode='w', encoding='UTF-8') as my_file:
            json.dump(my_dict, my_file)

    """
    Deserializes the JSON file to
    __objects only if the JSON file (__file_path) existis
    Otherwise do nothing.
    """
    def reload(self):
        if path.exists(self.__file_path):
            """ open the file and read the data """
            with open(self.__file_path, mode='r', encoding='UTF-8') as my_file:
                my_dict = json.load(my_file)
                from models.base_model import BaseModel
                for key, value in my_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
