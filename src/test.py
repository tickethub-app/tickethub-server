#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.organisation import Organisation

organisation = Organisation()
organisation.name ="Ussumane"
organisation.password = "Test"
organisation.email = "Email"
organisation.save()