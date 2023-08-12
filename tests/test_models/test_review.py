#!/usr/bin/python3
"""
    test reviews
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """
    Test case for Review class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup
        """
        cls.dummy_review = Review()
        cls.dummy_review.text = "test"
        cls.dummy_review.user_id = User().id
        cls.dummy_review.place_id = Place().id

    @classmethod
    def tearDownClass(cls):
        """
        Teardown
        """
        del cls.dummy_review

    def test_inheritance(self):
        """
        Test proper inheritance
        """
        self.assertIsInstance(self.dummy_review, BaseModel)
        self.assertTrue(hasattr(self.dummy_review, "id"))
        self.assertTrue(hasattr(self.dummy_review, "created_at"))
        self.assertTrue(hasattr(self.dummy_review, "updated_at"))

    def test_attributes(self):
        """
        Test attributes
        """
        self.assertTrue(hasattr(self.dummy_review, "text"))
        self.assertTrue(hasattr(self.dummy_review, "user_id"))
        self.assertTrue(hasattr(self.dummy_review, "place_id"))

if __name__ == "__main__":
    unittest.main()
