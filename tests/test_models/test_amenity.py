#!/usr/bin/python3
'''Amenity model unittest module'''
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import pep8


class TestAmenityModel(unittest.TestCase):
    '''Test amenity subclass model'''
    @classmethod
    def setUpClass(cls):
        '''Set up class'''
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Lisa"

    @classmethod
    def teardown(cls):
        '''Tear down class'''
        del cls.amenity1

    def tearDown(cls):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/amenity.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_is_subclass(self):
        '''Tests if subclass'''
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_init(self):
        ''''Tests initialization'''
        self.assertTrue(isinstance(self.amenity1, Amenity))

    def test_present(self):
        '''Tests docstring'''
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        '''Tests for needed attributes'''
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertTrue("updated_at" in self.amenity1.__dict__)
        self.assertTrue("created_at" in self.amenity1.__dict__)
        self.assertTrue("id" in self.amenity1.__dict__)

    def test_save(self):
        '''Tests save method'''
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_type(self):
        '''Tests attribute type'''
        amenity1_dict = self.amenity1.to_dict()
        self.assertEqual(self.amenity1.__class__.__name__, 'Amenity')
        self.assertIsInstance(amenity1_dict['created_at'], str)
        self.assertIsInstance(amenity1_dict['updated_at'], str)

    def test_to_dict(self):
            self.assertEqual('name' in dir(self.amenity1), True)

if __name__ == "__main__":
    unittest.main()
