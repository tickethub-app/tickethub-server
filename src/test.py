#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.organisation import Organisation
# from models.base import engine, Base, Session

# Base.metadata.create_all(engine)

# # 3 - create a new session
# session = Session()

organisation = Organisation()
organisation.name ="Ussumane"
organisation.password = "Test"
organisation.email = "Email"
print(organisation)
# session.add(organisation)
# session.commit()
# session.close()

storage.new(organisation)
storage.save()

# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://postgres:Paizinho01@localhost:5432/ticket_hub_dev")

# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# from sqlalchemy import Column, Integer, String

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)

#     def __repr__(self):
#        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
    
# print(User.__table__)

# Base.metadata.create_all(engine)