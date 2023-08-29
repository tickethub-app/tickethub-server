#!/usr/bin/python3
"""Get all the status"""
from api.v1.routes import app_routes
from flask import jsonify


@app_routes.route("/status", strict_slashes=False)
def status():
    """get status of the api"""
    return jsonify({"status": "OK"})
