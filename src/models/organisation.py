#!/usr/bin/python3
from models.base_model import BaseModel

class Organisation(BaseModel):
    """Organisation class extends BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)