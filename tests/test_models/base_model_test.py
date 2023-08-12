#!/usr/bin/env python3
""" unittest for base model """

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from uuid import UUID

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_type(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_name_type(self):
        self.assertIsInstance(self.model.name, str)

    def test_my_number_type(self):
        self.assertIsInstance(self.model.my_number, int)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        keys = ['id', 'created_at', 'updated_at', 'name', 'my_number', '__class__']
        model_dict = self.model.to_dict()
        self.assertTrue(all(key in model_dict for key in keys))

    def test_to_dict_created_at_format(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())


class TestBaseModelTwo(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()

    def test_id_generation(self):
        self.assertIsInstance(UUID(self.my_model.id), UUID)

    def test_str_representation(self):
        expected = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected)

    def test_to_dict_method(self):
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_from_dict_method(self):
        my_model_dict = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)

    def test_created_at_and_updated_at_types(self):
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


class TestModels(unittest.TestCase):
    def test_state(self):
        state = State()
        state.name = "Kenya"
        self.assertEqual(state.name, "Kenya")

    def test_city(self):
        city = City()
        city.name = "Nairobi"
        self.assertEqual(city.name, "Nairobi")

    def test_amenity(self):
        amenity = Amenity()
        amenity.name = "Free Wifi"
        self.assertEqual(amenity.name, "Free Wifi")

    def test_review(self):
        review = Review()
        review.text = "Good"
        self.assertEqual(review.text, "Good")

if __name__ == "__main__":
    unittest.main()
