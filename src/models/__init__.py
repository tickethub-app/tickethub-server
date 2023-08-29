# !/usr/bin/python3
from dotenv import load_dotenv
from models.base_model import BaseModel, Base
from models.organisation import Organisation
from models.engine.db_storage import DBStorage

load_dotenv()

storage = DBStorage()
storage.reload()