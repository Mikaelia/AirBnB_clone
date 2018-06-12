#!/usr/bin/python3
'''user model unittest module'''
import unittest
from models.user import User
import os
import pep8


class TestuserModel(unittest.TestCase):
    '''Testing user class'''
    @classmethod
    def setUpClass(cls):
        cls.user1 = User()
        cls.user1.email = 'User@user.com'
        cls.user1.password = 'password'
        cls.user1.first_name = 'Lisa'
        cls.user1.last_name = 'Olson'

    @classmethod
    def teardown(cls):
        del cls.user1

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/user.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_present(self):
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_values(self):
        self.assertTrue(self.user1.email, 'User@user.com')
        self.assertTrue(self.user1.password, 'password')
        self.assertTrue(self.user1.first_name, 'Lisa')
        self.assertTrue(self.user1.last_name, 'Olson')

    def test_init(self):
        self.assertTrue(isinstance(self.user1, User))

    def test_save(self):
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_to_dict(self):
        user1_dict = self.user1.to_dict()
        self.assertEqual(self.user1.__class__.__name__, 'User')
        self.assertIsInstance(user1_dict['email'], str)
        self.assertIsInstance(user1_dict['password'], str)
        self.assertIsInstance(user1_dict['first_name'], str)
        self.assertIsInstance(user1_dict['last_name'], str)

    def test_has_attributes(self):
        self.assertTrue('email' in self.user1.__dict__)
        self.assertTrue('first_name' in self.user1.__dict__)
        self.assertTrue('last_name' in self.user1.__dict__)
        self.assertTrue('password' in self.user1.__dict__)
        self.assertTrue('created_at' in self.user1.__dict__)
        self.assertTrue('updated_at' in self.user1.__dict__)


if __name__ == "__main__":
    unittest.main()
