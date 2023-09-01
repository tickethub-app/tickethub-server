#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.event import Event
from models.organisation import Organisation
from random import randint


variables = {"name": "ussumane", 
    "date": "2023-08-15 14:30:00", 
    "start_time": "09:00:00",
    "end_time": "12:00:00",
    "number_tickets": "100",
    "topic": "Test Event",
    "description": "This is a test event",
    "organisation_id": "1",
    }

organisation = Organisation(**variables)
organisation.save()
print(organisation.to_dict())

# obj = storage.get(Organisation, "2bb6fb9d-51e0-4e9c-b650-3064809f013a")
# print(obj)

print(storage.all(Organisation))