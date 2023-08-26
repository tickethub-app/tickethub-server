#!/usr/bin/python3
"""Event class"""
from models.base_model import BaseModel

class Event(BaseModel):
    """Event class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)