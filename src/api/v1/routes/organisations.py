#!/usr/bin/python3
"""Routes for the organisation endpoint"""
from models import storage
from models.organisation import Organisation
from api.v1.routes import app_routes
from flask import jsonify, abort, request
from sqlalchemy.exc import IntegrityError
from hashlib import md5


@app_routes.route("/organisations", strict_slashes=False)
def all_organisations():
    """Gets all organisation"""
    organisations = storage.all(Organisation)
    all_orgs = [org.to_dict() for org in organisations]
    return jsonify({"data": all_orgs}), 200


@app_routes.route("/organisations/<id>", strict_slashes=False)
def get_organisation(id):
    """get specific ORG"""
    org = storage.get(Organisation, id)
    if org is None:
        abort(404)
    return jsonify({"status": "success", "data": org.to_dict()}), 200


@app_routes.route("/organisations", methods=["POST"], strict_slashes=False)
def create_organisation():
    """Creates a new organisation"""
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Missing Organisation Data"}), 400
    keys = data.keys()
    if "name" not in keys:
        return jsonify({"status": "error", "message": "Missing Organisation Name"}), 400
    if "email" not in keys:
        return jsonify({"status": "error", "message": "Missing Organisation Email"}), 400
    if "password" not in keys:
        return jsonify({"status": "error", "message": "Missing Organisation Password"}), 400
    # Creates new Organisation
    try:
        new_org = Organisation(**data)
        new_org.password = md5(data.get("password").encode()).hexdigest()
        new_org.save()
        return jsonify({"status": "success", "data": new_org.to_dict()}), 201
    except IntegrityError as e:
        error_message = str(e.orig)
        if "duplicate key value violates unique constraint" in error_message:
            return jsonify({
                "error": "Email already exists",
                "message": "A user with the provided email already exists in the system."
                }), 409
        return jsonify({"error": "Some error occured"}), 500


@app_routes.route("/organisations/<id>", methods=["PUT"],
                  strict_slashes=False)
def update_organisation(id):
    """updates a organisation"""
    org = storage.get(Organisation, id)
    if org is None:
        abort(404)
    ignore = ['id', 'email', 'password', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(org, key, value)
    org.save()
    return jsonify({"status": "success", "data": org.to_dict()}), 200


@app_routes.route("/organisations/<id>", methods=["DELETE"])
def delete_organisation(id):
    """Deletes a organisation"""
    org = storage.get(Organisation, id)
    if org is None:
        abort(404)
    org.delete()
    return jsonify({"status": "success", "message": "Organisation removed with success!"})
