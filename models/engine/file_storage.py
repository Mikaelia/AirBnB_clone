#!/usr/bin/python3
'''FileStorage class module'''
import json


class FileStorage():
    '''FileStorage class'''
        __file_path = 'file.json'
        __objects = {}
    def all(self):
        '''returns the dictionary __objects'''
        return __objects
    def new(self, obj):
        '''sets class.id key with obj value'''
        __objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        '''serializes __objects to the JSON file'''
        '''turning __objects into dict'''
        mydict = {}
        for k, v  in __objects.items()
            mydict[k] = v.to_dict()
        with open(__file_path, mode='w+', encoding='utf-8') as f:
            json.dump(mydict, f)
    def reload(self):
        '''deserializes the JSON file to __objects if file exists'''
        try:
            with open(self.__file_path, mode='r') as f:
                self.__objects = json.load(f)
                '''eval'''
        except FileNotFoundError:
            pass
