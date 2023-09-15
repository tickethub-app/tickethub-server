#!/usr/bin/python3
"""Auth Routes"""
from api.v1.routes import app_routes
from flask import jsonify, request
from hashlib import md5
from models import storage
from models.organisation import Organisation


@app_routes.route("/auth/login", methods=["POST"])
def login():
    """Login with email and password"""
    data = request.get_json()
    if data is None:
        return jsonify({"status": "error",
                        "message": "Missing Organisation Data"}), 400
    keys = data.keys()
    if "email" not in keys:
        return jsonify({"status": "error",
                        "message": "Missing Organisation Email"}), 400
    if "password" not in keys:
        return jsonify({"status": "error",
                        "message": "Missing Organisation Password"}), 400
    try:

        org = storage.get_by_key(Organisation, key="email",
                                 value=data.get("email"))
        if not org:
            raise Exception()
        if org.password != md5(data.get("password").encode()).hexdigest():
            raise Exception()
        auth_token = org.encode_auth_token(org.id)
        if auth_token:
            responseObj = {'status': 'success',
                           'message': 'successfully logged in',
                           'auth_token': str(auth_token)}
            return jsonify(responseObj), 200
        responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
        return jsonify(responseObject), 404
    except Exception as e:
        print(e)
        responseObj = {'status': 'error', 'message': 'Try again'}
        return jsonify(responseObj), 500
