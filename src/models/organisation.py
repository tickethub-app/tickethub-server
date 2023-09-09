#!/usr/bin/python3
import datetime
import jwt
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5
from os import getenv


class Organisation(BaseModel, Base):
    """Organisation class extends BaseModel"""
    __tablename__ = "organisations"

    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr(self, name, value):
        """Enconding user password"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr(self, name, value)

    def encode_auth_token(self, user_id):
        """Generates the Auth Token
        : return -> string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat':  datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, getenv('SECRET_KEY'), algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, getenv('SECRET_KEY'))
            return payload.get('sub')
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
