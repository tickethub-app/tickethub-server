#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Organisation(BaseModel, Base):
    """Organisation class extends BaseModel"""
    __tablename__ = "organisations"
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)