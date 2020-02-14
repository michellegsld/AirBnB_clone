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
        key = str(type(self).__name) + str(self.id)
        __objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w+') as fil:
            fil.write(json.dumps(self.__objects))

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as fil:
                return json.loads(fil.read())
