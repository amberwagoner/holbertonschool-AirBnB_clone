#!/usr/bin/python3
""" Class that serializes instances to JSON file and vice versa """
import json
from models.base_model import BaseModel
from os import path


class FileStorage:
    """ Our storage engine """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns __objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__
        obj = FileStorage.__objects["{}.{}".format(key, obj.id)]

    def save(self):
        """ Serializes __objects to the JSON file in path __file_path """
        with open(self.__file_path, mode="w") as f:
            dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                dict = json.load(f)
                for key, value in dict.items():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
