#!/usr/bin/python3
'''Amenity model unittest module'''
import unittest
from models.amenity import Amenity
import os
import pep8


class TestAmenityModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Lisa"

    @classmethod
    def teardown(cls):
        del cls.amenity1

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/amenity.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_present(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "name"))

    def test_init(self):
        self.assertTrue(isinstance(self.amenity1, Amenity))

    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        amenity1_dict = self.amenity1.to_dict()
        self.assertEqual(self.amenity1.__class__.__name__, 'Amenity')
        self.assertIsInstance(amenity1_dict['created_at'], str)
        self.assertIsInstance(amenity1_dict['updated_at'], str)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)


if __name__ == "__main__":
    unittest.main()
