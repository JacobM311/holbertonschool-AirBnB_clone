#!/usr/bin/python3
"""
Contains the FileStorage class
"""

from os import path
import json


class FileStorage:
    """File Storage Class"""

    # string - path to the JSON file
    __file_path = 'file.json'
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """return content of __objects attribute"""
        return self.__objects

    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        if path.exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as f:
                self.__objects = json.load(f)
