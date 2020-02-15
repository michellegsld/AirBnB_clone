#!/usr/bin/python3
"""
file_storage.py
FileStorage Class
"""
import json
import os.path


class FileStorage:
    """
    Serializes instances to a JSON file as storage
    Deserializes JSON file to instances to recreate saved instances
    Contains the class attributes:
    - __file_path -> String. Path to JSON file.
    - __objects -> Dictionary. To contain objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return type(self).__objects

    def new(self, obj):
        """
        Populates the __objects dictionary
        Uses this format for creating the keys of each value:
        <class name of object>.<id of object>
        """
        key = str(type(obj).__name__) + '.' + str(obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary __objects to the JSON file
        To do so, a copy of __objects must be made in order to:
        -> save dictionary of attributes of object/instance within copy
        """
        temp = {}
        temp.update(type(self).__objects)
        for k, v in temp.items():
            temp[k] = v.to_dict()
        with open(self.__file_path, 'w+') as fil:
            json.dump(temp, fil)

    def reload(self):
        """
        Deserializes the JSON file back into __objects
        To do so, it has to re-create the object using:
        -> dictionarys of attributes saved as the values within the dict
        """
        if os.path.isfile(type(self).__file_path):
            from models.base_model import BaseModel
            with open(self.__file_path) as fil:
                dic = json.load(fil)
                for k, v in dic.items():
                    FileStorage.__objects[k] = BaseModel(**v)
