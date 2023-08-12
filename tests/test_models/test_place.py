#!/usr/bin/python3
"""Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        super().setUp()  # Call parent class's setUp method
        self.place = Place()

    def test_instantiation_creates_instance(self):
        self.assertEqual(Place, type(self.place))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.place, models.storage.all().values())

    # ... Rest of the instantiation tests ...


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    def setUp(self):
        super().setUp()  # Call parent class's setUp method
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save_updates_updated_at(self):
        pl = Place()
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    # ... Rest of the save tests ...


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertIsInstance(Place().to_dict(), dict)

    # ... Rest of the to_dict tests ...

if __name__ == "__main__":
    unittest.main()
