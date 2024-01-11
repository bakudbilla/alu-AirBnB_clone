#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    """serializes and deserialzes json files"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary of <class>.<id> : object instance"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new obj to existing dictionary of instances"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Save obj dictionaries to json file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """If json file exists, convert obj dicts back to instances"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
