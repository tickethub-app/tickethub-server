#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.organisation import Organisation
from random import randint

organisation = Organisation()
organisation.name = "Ussumane" 
organisation.password = "Test"
organisation.email = "Email" + str(randint(0, 9999))
# organisation.save()

objs = storage.all(Organisation)
for obj in objs:
    print(obj)
