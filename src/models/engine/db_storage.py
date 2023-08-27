#!/usr/bin/python3
"""DBStorage class"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Database storage class system"""
    __engine = None
    __session = None
    
    def __init__(self):
        """Constructor of the DB Storage"""
        HUB_PSQL_USER = getenv("HUB_PSQL_USER")
        HUB_PSQL_PWD = getenv("HUB_PSQL_PWD")
        HUB_PSQL_HOST = getenv("HUB_PSQL_HOST")
        HUB_PSQL_PORT = getenv("HUB_PSQL_PORT")
        HUB_PSQL_DB = getenv("HUB_PSQL_DB")
        HUB_ENV = getenv("HUB_ENV")
        print("postgresql://{}:{}@{}:{}/{}".format(
            HUB_PSQL_USER,
            HUB_PSQL_PWD,
            HUB_PSQL_HOST,
            HUB_PSQL_PORT,
            HUB_PSQL_DB
        ))
        self.__engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(
            HUB_PSQL_USER,
            HUB_PSQL_PWD,
            HUB_PSQL_HOST,
            HUB_PSQL_PORT,
            HUB_PSQL_DB
        ))

    def reload(self):
        """reload the database conection"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def new(self, obj):
        """Adds new object"""
        self.__session.add(obj)

    def save(self):
        self.__session.commit()