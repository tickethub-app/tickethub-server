#!/usr/bin/python3
"""Main Entrance for the api"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.routes import app_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(app_routes)


@app.teardown_appcontext
def close_db(error):
    """Close the session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handling the 404 error"""
    return jsonify({"status": "not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
