#!/usr/bin/python3
'''FileStorage class module'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.revew import Review

class FileStorage():
    '''FileStorage class'''
    __file_path = 'file.json'
    __objects = {}
    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects
    def new(self, obj):
        '''sets class.id key with obj value'''
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        '''serializes __objects to the JSON file'''
        mydict = {}
        for k, v  in FileStorage.__objects.items():
            mydict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(mydict, f)
    def reload(self):
        '''deserializes the JSON file to __objects if file exists'''
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                jdict = json.load(f)
            for k, v in jdict.items():
                newobj = eval(v['__class__'])(**v)
                FileStorage.__objects[k] = newobj
        except FileNotFoundError:
            pass
