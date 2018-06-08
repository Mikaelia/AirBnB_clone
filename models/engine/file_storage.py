#!/usr/bin/python3
'''FileStorage class module'''
import json


class FileStorage():
    '''FileStorage class'''
    def __init__(self, file_path=None, objects=None):
        '''Initialization of FileStorage instance
            Args:
                file_path (str): path to the JSON file
                objects (dict): will store all objects by <class name>.id
        '''
        self.__file_path = file_path
        self.__objects = objects
    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects
    def new(self, obj):
        '''sets class.id key with obj value'''
        self.__objects[self.__class__.__name__] = obj
    def save(self):
        '''serializes __objects to the JSON file'''
        with open(self.__file_path) as f:
            json.dump(self.__objects, f)
    def reload(self):
        '''deserializes the JSON file to __objects if file exists'''
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except OSError:
            pass
