#!/usr/bin/python3
'''City model unittest module'''
import unittest
from models.city import City
import os
import pep8


class TestCityModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "lisa"
        cls.city1.state_id = 'State'

    @classmethod
    def teardown(cls):
        del cls.city1

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/city.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_present(self):
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(City, "__init__"))
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_values(self):
        self.assertTrue(self.city1.state_id, 'State')
        self.assertTrue(self.city1.name, 'lisa')

    def test_init(self):
        self.assertTrue(isinstance(self.city1, City))

    def test_save(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        city1_dict = self.city1.to_dict()
        self.assertEqual(self.city1.__class__.__name__, 'City')
        self.assertIsInstance(city1_dict['created_at'], str)
        self.assertIsInstance(city1_dict['updated_at'], str)
        self.assertIsInstance(city1_dict['state_id'], str)
        self.assertIsInstance(city1_dict['name'], str)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

if __name__ == "__main__":
    unittest.main()
