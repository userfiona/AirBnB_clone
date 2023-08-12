#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from models.city import City

class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_instantiation_creates_instance(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    # ... Rest of the instantiation tests ...


class TestCitySave(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    # ... Setup and teardown methods ...

    def test_one_save_updates_updated_at(self):
        cy = City()
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    # ... Rest of the save tests ...


class TestCityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(City().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        cy = City()
        keys_to_check = ['id', 'created_at', 'updated_at', '__class__']
        for key in keys_to_check:
            self.assertIn(key, cy.to_dict())

    # ... Rest of the to_dict tests ...

if __name__ == "__main__":
    unittest.main()
