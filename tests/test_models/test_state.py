#!/usr/bin/python3
'''state model unittest module'''
import unittest
from models.state import State
import os
import pep8


class TeststateModel(unittest.TestCase):
    '''Testing state class'''
    @classmethod
    def setUpClass(cls):
        cls.state1 = State()
        cls.state1.name = "Mikaela"

    @classmethod
    def teardown(cls):
        del cls.state1

    def tearDown(cls):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/state.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_is_subclass(self):
        '''Tests if subclass'''
        self.assertTrue(issubclass(self.state1.__class__, State), True)

    def test_present(self):
        '''Test for doc string'''
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        '''Test for attributes'''
        self.assertTrue(hasattr(State, "name"))

    def test_values(self):
        '''Test attribute value'''
        self.assertTrue(self.state1.name, 'Mikaela')

    def test_init(self):
        '''Test for object initialization'''
        self.assertTrue(isinstance(self.state1, State))

    def test_save(self):
        '''Test save method'''
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        '''Test dict method'''
        state1_dict = self.state1.to_dict()
        self.assertEqual(self.state1.__class__.__name__, 'State')
        self.assertIsInstance(state1_dict['name'], str)

    def test_has_attributes(self):
        '''Test for attributes in dictionary'''
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)


if __name__ == "__main__":
    unittest.main()
