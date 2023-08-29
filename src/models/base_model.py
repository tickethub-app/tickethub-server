#!/usr/bin/python3
"""base model class"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()

class BaseModel:
    """"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """base model constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """to string method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """default save method"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()
    
    def delete(self):
        """Delete the object from the session"""
        from models import storage
        storage.delete(self)
        storage.save()
    
    def to_dict(self):
        """transforms the current object into dict"""
        return self.__dict__
    
