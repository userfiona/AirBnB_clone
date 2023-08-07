"""
BaseModal class
"""
import uuid
from datetime import datetime,timedelta
import json

class BaseModel():
    """
    initiate the class with these atributes
    @id - uniq id 
    @created_at - time for instance creation
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print string rep if object """
        return(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """
        updates the public instance atribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        return json.dumps(self.__dict__)
