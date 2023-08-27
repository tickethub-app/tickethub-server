#!/usr/bin/python3
"""Event class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Time, Integer, ForeignKey

class Event(BaseModel, Base):
    """Event class"""
    __tablename__ = "events"
    date = Column(DateTime, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    number_tickets = Column(Integer, nullable=False)
    topic = Column(String(128), nullable=False)
    description=Column(String(1024), nullable=False)
    organisation_id = Column(String(60), ForeignKey('organisations.id'), nullable=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)