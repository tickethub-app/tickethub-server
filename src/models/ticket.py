#!/usr/bin/python3
"""Ticket class"""
from models.base_model import BaseModel

class Ticket(BaseModel):
    """Ticket"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)