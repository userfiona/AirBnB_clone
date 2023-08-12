#!/usr/bin/python3
"""
    This is a module test from Amenity class and your methods.
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attribute_initialization(self):
        self.assertEqual(self.amenity.name, '')

    def test_instance_type(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_property_assignment(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_edge_cases(self):
        self.amenity.name = ""  # Test an empty name
        self.assertEqual(self.amenity.name, "")

        long_name = "a" * 256  # Test a very long name
        self.amenity.name = long_name
        self.assertEqual(self.amenity.name, long_name)

    def test_property_validation(self):
        with self.assertRaises(ValueError):
            self.amenity.name = None

    def test_equality_comparison(self):
        amenity1 = Amenity(name="Gym")
        amenity2 = Amenity(name="Gym")
        self.assertEqual(amenity1, amenity2)

if __name__ == "__main__":
    unittest.main()
