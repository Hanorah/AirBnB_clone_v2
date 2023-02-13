#!/usr/bin/python3

"""FileStorage class definition"""

import json
import models


class FileStorage:
    """Serializes instances to JSON file and deserializes to JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""

        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class>.id
            Arguments:
                obj : An instance object.
        """

        k = str(obj.__class__.__name__) + "." + str(obj.id)
        v_dict = obj
        FileStorage.__objects[k] = v_dict
    
    def save(self):
        """Serializes __objects attribute to JSON file"""

        objects_dict = {}

        for k, v in FileStorage.__objects.items():
            objects_dict[k] = v.to_dict()
        
        with open(FileStorage.__file__path, mode="w", encoding="UTF8") as fd:
            json.dump(objects_dict, fd)
    
    def reload(self):
        """Deserializes the JSON file to __objects."""

        try:
            with open(FileStorage.__file__path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for k, v in FileStorage.__objects.items():
                class_name = v["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[k] = class_name(**v)

        except FileNotFoundError:
            pass