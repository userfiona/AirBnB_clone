#!/usr/bin/python3

"""
get the unittest module
get the patch, mock_open models from unittest.mock
get the filestorage model
get the Basemodel model
"""
import unittest
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json

"""
class to test the FileStorage model
"""


class TestFileStorage(unittest.TestCase):

    """
    setup method to create an instance of the filestorage
    """
    def setUp(self):
        self.storage = FileStorage()

    """
    test all function to see if what it returns is an
    instance of dict class
    """
    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

    """
    test new method  to see if it converts the key
    to (obj.__class__.__name__).(obj.id)
    """
    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    """
    test save method using mock module to simulate
    real writing to a file
    covert dict to json object
    """
    @patch('json.dump')
    def test_save(self, mock_dump):
        obj = BaseModel()
        self.storage.new(obj)
        with patch('builtins.open', mock_open()) as m:
            self.storage.save()
            m.assert_called_once_with(self.storage._FileStorage__file_path,
                                      mode='w', encoding='UTF-8')
            mock_dump.assert_called_once()

    """
    test reload method using mock module to simulate
    real reading from a file
    covert json object to dict
    """
    @patch('json.load')
    def test_reload(self, mock_load):
        json_data = {
                "BaseModel.1234": {
                    "__class__": "BaseModel",
                    "id": "1234",
                    "created_at": "2023-08-28T21:07:25.047372",
                    "updated_at": "2017-09-28T21:07:25.047372"
                    }
                }
        mock_load.return_value = json_data
        with patch('builtins.open', mock_open(read_data=json.
                                              dumps(json_data))):
            self.storage.reload()
            # self.assertEqual(len(self.storage._FileStorage__objects), 1)
            """self.assertIsInstance(self.storage._FileStorage__objects
            ["BaseModel.1234"], BaseModel)"""


if __name__ == '__main__':
    unittest.main()
