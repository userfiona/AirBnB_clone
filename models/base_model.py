#!/usr/bin/python3

"""
get the uuid for ad=signing uniq id to each instance created
get datetime to record created and updated time of each object
get json for use in serialization and deserialization
"""


import uuid
from datetime import datetime
import json


"""
BaseModal class
"""


class BaseModel():
    """
    initiate the class with these atributes
    @id - uniq id
    @created_at - time for instance creation
    """
    def __init__(self):
        """
        initiate the base class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print string rep if object """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the public instance atribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return the dictionary of and object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
