#!/usr/bin/python3
"""Blueprints of the application"""

from flask import Flask, Blueprint, request
from functools import wraps
import jwt
from os import getenv


app_routes = Blueprint("app_routes", __name__, url_prefix="/api/v1")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"status": "error", "message": "Token is missing"}), 401
        token = token.replace('Bearer ', '')
        try:
            data = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
        except:
            return jsonify({"message": "Invalid Token"}), 403
        return f(*args, **kwargs)
    return decorated

"""Add the routes here"""
from api.v1.routes.index import *
from api.v1.routes.organisations import *
from api.v1.routes.tickets import *
from api.v1.routes.auth import *
