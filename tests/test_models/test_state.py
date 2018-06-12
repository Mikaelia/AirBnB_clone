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

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/state.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_present(self):
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(State, "name"))

    def test_values(self):
        self.assertTrue(self.state1.name, 'Mikaela')

    def test_init(self):
        self.assertTrue(isinstance(self.state1, State))

    def test_save(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        state1_dict = self.state1.to_dict()
        self.assertEqual(self.state1.__class__.__name__, 'State')
        self.assertIsInstance(state1_dict['name'], str)

    def test_has_attributes(self):
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)

if __name__ == "__main__":
    unittest.main()
