#!/usr/bin/python3
'''Place model unittest module'''
import unittest
from models.place import Place
import os
import pep8


class TestPlaceModel(unittest.TestCase):
    '''Test Place class'''

    @classmethod
    def setUpClass(cls):
        '''Setup method'''
        cls.place1 = Place()
        cls.place1.city_id = 'San Francisco'
        cls.place1.user_id = '1'
        cls.place1.name = 'Holberton'
        cls.place1.description = 'School'
        cls.place1.number_rooms = 5
        cls.place1.number_bathrooms = 5
        cls.place1.max_guest = 5
        cls.place1.price_by_night = 500
        cls.place1.latitude = 1.0
        cls.place1.longitude = 1.0
        cls.place1.amenity_ids = [2, 3]

    @classmethod
    def teardown(cls):
        '''Teardown method'''
        del cls.place1

    def tearDown(cls):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/place.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_is_subclass(self):
        '''Tests if subclass'''
        self.assertTrue(issubclass(self.place1.__class__, Place), True)

    def test_present(self):
        '''Test doc string'''
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        '''Testing for correct attributes'''
        self.assertTrue(hasattr(Place, "__init__"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_init(self):
        '''Testing correct initialization'''
        self.assertTrue(isinstance(self.place1, Place))

    def test_save(self):
        '''Test correct save'''
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        place1_dict = self.place1.to_dict()
        self.assertEqual(self.place1.__class__.__name__, 'Place')
    def test_type(self):
        '''Test for correct type'''
        place1_dict = self.place1.to_dict()
        self.assertIsInstance(place1_dict['created_at'], str)
        self.assertIsInstance(place1_dict['updated_at'], str)
        self.assertIsInstance(place1_dict['name'], str)
        self.assertIsInstance(place1_dict['description'], str)
        self.assertIsInstance(place1_dict['number_rooms'], int)
        self.assertIsInstance(place1_dict['number_bathrooms'], int)
        self.assertIsInstance(place1_dict['max_guest'], int)
        self.assertIsInstance(place1_dict['price_by_night'], int)
        self.assertIsInstance(place1_dict['latitude'], float)
        self.assertIsInstance(place1_dict['longitude'], float)
        self.assertIsInstance(place1_dict['amenity_ids'], list)

    def test_has_attributes(self):
        '''Test for attributes in dictionary'''
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)


if __name__ == "__main__":
    unittest.main()
