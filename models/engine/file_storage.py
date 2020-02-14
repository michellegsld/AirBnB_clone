#!/usr/bin/python3
"""handling JSON files """
import json
import os.path


class FileStorage():
    __file_path = file.json
    __objects = {}

    def all(self):
        return type(self).__objects

    def new(self, obj):
        key = str(type(obj).__name) + '.' + str(obj.id)
        type(self).__objects[key] = obj

    def save(self):
        temp = {}
        temp.update(type(self).__objects)
        for k, v in temp.items():
            temp[k] = v.to_dict()
        with open(self.__file_path, 'w+') as fil:
            json.dump(temp, fil)

    def reload(self):
        if os.path.isfile((type)self.__file_path):
            with open(self.__file_path) as fil:
                json.load(fil)
