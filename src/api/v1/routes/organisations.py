#!/usr/bin/python3
"""Routes for the organisation endpoint"""
from models import storage
from models.organisation import Organisation
from api.v1.routes import app_routes
from flask import jsonify


@app_routes.route("/organisations", strict_slashes=False)
def index():
    """Gets all organisation"""
    organisations = storage.all()
    return jsonify(organisations), 200


@app_routes.route("/organisations/<id>", strict_slashes=False)
def get_organisation(id):
    """get specific ORG"""
    return jsonify({"status": "success"}), 200


@app_routes.route("/organisations", methods=["POST"], strict_slashes=False)
def create_organisation():
    """Creates a new organisation"""
    return jsonify({}), 201


@app_routes.route("/organisations/<id>", methods=["PUT"],
                  strict_slashes=False)
def update_organisation(id):
    """updates a organisation"""
    return jsonify({})


@app_routes.route("/organisations/<id>", methods=["DELETE"])
def delete_organisation(id):
    """Deletes a organisation"""
    return jsonify({})
