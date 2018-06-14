#!/usr/bin/python3
'''Base model unittest module'''
import unittest
from models.base_model import BaseModel
import os
import pep8


class TestBaseModel(unittest.TestCase):
    '''Tests BaseModel class'''

    @classmethod
    def setUpClass(cls):
        '''Setup class'''
        cls.base1 = BaseModel()
        cls.base1.name = "Mikaela"

    @classmethod
    def teardown(cls):
        '''Teardown class'''
        del cls.base1

    def tearDown(self):
        '''Removes file'''
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/base_model.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Error")

    def test_checking_for_functions(self):
        '''Checks for docs'''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attributes(self):
        '''Checks BaseModel methods'''
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue("updated_at" in self.base1.__dict__)
        self.assertTrue("created_at" in self.base1.__dict__)
        self.assertTrue("id" in self.base1.__dict__)

    def test_init(self):
        '''Tests initialization'''
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        '''Tests save functionality'''
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        '''Tests to_dict method'''
        self.assertEqual('name' in dir(self.base1), True)

    def test_type(self):
        '''Tests attribute type'''
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
