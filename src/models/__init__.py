# !/usr/bin/python3
from models.base_model import BaseModel, Base
from models.organisation import Organisation
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()