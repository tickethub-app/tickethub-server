#!/usr/bin/python3
"""base model class"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """"""
    def __init__(self, *args, **kwargs):
        """base model constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """to string method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """default save method"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """transforms the current object into dict"""
        return self.__dict__
    
