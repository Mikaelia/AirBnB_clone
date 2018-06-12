#!/usr/bin/python3
'''review model unittest module'''
import unittest
from models.review import Review
import os
import pep8


class TestReviewModel(unittest.TestCase):
    '''Testing review class'''
    @classmethod
    def setUpClass(cls):
        cls.review1 = Review()
        cls.review1.place_id = "This"
        cls.review1.user_id = 'That'
        cls.review1.text = 'Other'

    @classmethod
    def teardown(cls):
        del cls.review1

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        '''Pep8 style test'''
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/review.py'])
        self.assertEqual(f.total_errors, 0, "Style Error")

    def test_present(self):
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(hasattr(Review, "user_id"))

    def test_values(self):
        self.assertTrue(self.review1.place_id, 'This')
        self.assertTrue(self.review1.user_id, 'That')
        self.assertTrue(self.review1.text, 'Other')

    def test_init(self):
        self.assertTrue(isinstance(self.review1, Review))

    def test_save(self):
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_to_dict(self):
        review1_dict = self.review1.to_dict()
        self.assertEqual(self.review1.__class__.__name__, 'Review')
        self.assertIsInstance(review1_dict['created_at'], str)
        self.assertIsInstance(review1_dict['updated_at'], str)
        self.assertIsInstance(review1_dict['place_id'], str)
        self.assertIsInstance(review1_dict['user_id'], str)
        self.assertIsInstance(review1_dict['text'], str)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review1.__dict__)
        self.assertTrue('place_id' in self.review1.__dict__)
        self.assertTrue('created_at' in self.review1.__dict__)
        self.assertTrue('updated_at' in self.review1.__dict__)
        self.assertTrue('user_id' in self.review1.__dict__)
        self.assertTrue('text' in self.review1.__dict__)


if __name__ == "__main__":
    unittest.main()
