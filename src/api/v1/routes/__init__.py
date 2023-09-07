#!/usr/bin/python3
"""Blueprints of the application"""

from flask import Flask, Blueprint

app_routes = Blueprint("app_routes", __name__, url_prefix="/api/v1")

"""Add the routes here"""
from api.v1.routes.index import *
from api.v1.routes.organisations import *
from api.v1.routes.events import *
from api.v1.routes.tickets import *
from api.v1.routes.auth import *
