#!/usr/bin/python3
"""
get datetime module from datetime
get the unittest module
get os use os.path module to use to check if file exist
in teardown method to remove it
get the BaseModel module
"""
from datetime import datetime
from models.base_model import BaseModel
import os
import unittest

"""
TestBaseModel class
"""


class TestBaseModel(unittest.TestCase):

    """ set up function"""
    @classmethod
    def setUpClass(cls):
        cls.my_model = BaseModel()
        cls.my_model_2 = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    """ test if id is assigned """
    def test_id(self):
        self.assertTrue(TestBaseModel.my_model.id)

    """test id is a string"""
    def test_id_type(self):
        self.assertTrue(type(TestBaseModel.my_model.id) == str)

    """ test id is uniq"""
    def test_id_uniq(self):
        self.assertTrue(TestBaseModel.my_model.id !=
                        TestBaseModel.my_model_2.id)

    """ test created at is assigned """
    def test_created_at(self):
        self.assertTrue(TestBaseModel.my_model.created_at)

    """
    test created date is datetime instance
    """
    def test_created_at_is_datetime(self):
        self.assertIsInstance(TestBaseModel.my_model.created_at, datetime)

    """ test updated_at at is assigned """
    def test_updated_at(self):
        self.assertTrue(TestBaseModel.my_model.updated_at)

    """
    test updated date is datetime instance
    """
    def test_updated_at_is_datetime(self):
        self.assertIsInstance(TestBaseModel.my_model.updated_at, datetime)

    """test __str__ of an object"""
    def test_str(self):
        exOutPut = "[{}] ({}) {}".format(TestBaseModel.my_model.__class__
                                         .__name__,
                                         TestBaseModel.my_model.id,
                                         TestBaseModel.my_model.__dict__)
        output = str(TestBaseModel.my_model)
        self.assertEqual(output, exOutPut)

    """
    test save method check if the updated_at value changes
    """
    def test_save(self):
        firstUpdatedValue = TestBaseModel.my_model.updated_at
        TestBaseModel.my_model.save()
        secondUpdatedValue = TestBaseModel.my_model.updated_at
        self.assertTrue(type(TestBaseModel.my_model.id) == str)
        self.assertTrue(firstUpdatedValue != secondUpdatedValue)

    """
    test to_dict method
    confirm __class__ is added to the dict
    confirm created_at and updated_at are in isoformat
    """
    def test_to_dict_method(self):
        obj_dict = TestBaseModel.my_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], TestBaseModel.my_model.id)
        self.assertEqual(obj_dict['created_at'],
                         TestBaseModel.my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         TestBaseModel.my_model.updated_at.isoformat())

    """
    Test creating BaseModel from dictionary
    """
    def test_create_BaseModel_Dict(self):
        my_dict = TestBaseModel.my_model.to_dict()
        my_model = BaseModel(my_dict)
        self.assertTrue(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertTrue(my_model.id !=
                        TestBaseModel.my_model_2.id)

    """
    Set up teardown method
    """
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")


"""
if test is executed it runs as main
but if it is imported it does not execute
"""
if __name__ == "__main__":
    unittest.main()
