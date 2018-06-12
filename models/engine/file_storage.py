#!/usr/bin/python3
'''FileStorage class module'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    '''FileStorage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary {<class_name>.<id>:<class_instance>}'''
        return self.__objects

    def new(self, obj):
        '''Formats key and assings corresponding object value'''
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''Serializes __objects dict and stores in JSON file'''
        mydict = {}
        for k, v in self.__objects.items():
            mydict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w+') as f:
            json.dump(mydict, f)

    def reload(self):
        '''Deserializes JSON file to dict with obj instances if file exists'''
        try:
            with open(self.__file_path, mode='r') as f:
                jdict = json.load(f)
            for k, v in jdict.items():
                newobj = eval(v['__class__'])(**v)
                self.__objects[k] = newobj
        except FileNotFoundError:
            pass
