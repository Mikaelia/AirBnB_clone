#!/usr/bin/python3
'''Unittest for FileStorage'''

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import pep8
import json

class TestFileStorageModel(unittest.TestCase):
    '''Testing File Storage'''

    @classmethod
    def setUp(cls):
        '''Sets up class'''
        pass

    @classmethod
    def tearDown(cls):
        '''Tears down class'''
        pass

    def tearDown(self):
        '''Removes json file'''
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        '''Tests pep8 styling'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Error")

    def test_all(self):
        '''Checks all method'''
        st = FileStorage()
        dic = st.all()
        self.assertIsNotNone(dic)
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, st._FileStorage__objects)


    def test_new(self):
        '''Tests new method'''
        s = FileStorage()
        dic = s.all()
        maine = State()
        maine.name = "Maine"
        s.new(maine)
        key = maine.__class__.__name__ + "." + str(maine.id)
        self.assertIsNotNone(dic[key])

    def test_reload(self):
        '''Tests reload method'''
        st = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(st.reload(), None)

