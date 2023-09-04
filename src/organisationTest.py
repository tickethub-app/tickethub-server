#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.organisation import Organisation
from random import randint
from hashlib import md5

variables = {"name": "ussumane", "email": "test@test.co.mz", "test": "new variable"}
password = md5("ussboy".encode()).hexdigest()

organisation = Organisation(**variables)
organisation.password = password
organisation.save()
print(organisation.to_dict())

# obj = storage.get(Organisation, "2bb6fb9d-51e0-4e9c-b650-3064809f013a")
# print(obj)

#print(storage.all(Organisation))
