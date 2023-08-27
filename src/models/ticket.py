#!/usr/bin/python3
"""Ticket class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean

class Ticket(BaseModel):
    """Ticket"""
    __tablename__ = "tickets"
    attendee_name = Column(String(128), nullable=False)
    event_id = Column(String(60), ForeignKey("events.id"), nullable=False)
    attended = Column(Boolean, nullable=False)
    field = Column(String(128), nullable=True)   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)