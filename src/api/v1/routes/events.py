#!/usr/bin/python3
import html
import os
import re
from datetime import datetime, time
from models import storage
from models.event import Event
from api.v1.routes import app_routes
from flask import jsonify, abort, request
from werkzeug.utils import secure_filename
from uuid import uuid4


@app_routes.route("/events", strict_slashes=False)
def index():
    "Get all events"
    events = storage.all(Event)
    all_events = [event.to_dict() for event in events]
    return jsonify({"data": all_events}), 200


@app_routes.route("/events/<id>", strict_slashes=False)
def get_event(id):
    """Get a specific event using id"""

    event = storage.get(Event, id)
    if event is None:
        abort(404)
    return jsonify({"status": "success", "data": event.to_dict()}), 200


@app_routes.route("/events/search", strict_slashes=False)
def search_events():
    search_term = request.args.get("name")

    if not search_term:
        return jsonify({"status": "error", "message": "No input search term"}), 400

    matching_events = storage.session.query(Event).filter(
        Event.name.islike(f"%{search_term}%")).all()

    event_data = [{"id": event.id, "topic": event.topic,
                   "date": event.date} for event in matching_events]

    return jsonify({"status": "success", "events": event_data}), 200


@app_routes.route("/events", methods=["POST"], strict_slashes=False)
def create_event():
    """Create a new event"""
    data = request.form.to_dict()
    image_file = request.files.get("image")
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400

    required_attributes = ["date", "start_time", "end_time",
                           "number_tickets", "description", "organisation_id"]

    missing_attributes = [
        attr for attr in required_attributes if attr not in data]
    if image_file is None:
        missing_attributes.append('image')
    if missing_attributes:
        return jsonify({"status": "error", "message": f"Missing an attributes: {','.join(missing_attributes)}"})

    # sanitizing input data to prevent XSS
    cleaned_data = {
        "date": html.escape(data.get("date", "")),
        "start_time": html.escape(data.get("start_time", "")),
        "end_time": html.escape(data.get("end_time", "")),
        "number_tickets": html.escape(data.get("number_tickets", "")),
        "topic": html.escape(data.get("topic", "")),
        "description": html.escape(data.get("description", "")),
        "organisation_id": html.escape(data.get("organisation_id", ""))
    }

    # validate data
    if not re.match(r"\d{4}-\d{2}-\d{2}$", cleaned_data.get("date", "")):
        return jsonify({"status": "error", "message": "Invalid date format"}), 400

    # Validate time format (HH:MM:SS)
    for time_field in ["start_time", "end_time"]:
        if not re.match(r"\d{2}:\d{2}:\d{2}$", cleaned_data.get(time_field, "")):
            return jsonify({"status": "error", "message": f"Invalid {time_field} format"}), 400

    # Validate number_tickets is a positive integer
    try:
        num_tickets = int(cleaned_data.get("number_tickets", ""))
        if num_tickets <= 0:
            return jsonify({"status": "error", "message": "Number of tickets must be a positive integer"}), 400
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid number of tickets"}), 400

    # save the uploaded image file
    if image_file:
        filename = secure_filename(image_file.filename)
        filename = f"{str(uuid4()).replace('-', '_')}_{filename}"
        image_path = os.path.join("uploads", filename)
        image_file.save(image_path)
        cleaned_data["image"] = image_path

    new_event = Event(**cleaned_data)
    # print(new_event)
    storage.new(new_event)
    storage.save()

    return jsonify({"message": "Event created successfully"}), 201


@app_routes.route("/events/<id>", methods=["PUT"], strict_slashes=False)
def update_event(id):
    """Updates  event"""
    return jsonify({})


@app_routes.route("/events/<id>", methods=["DELETE"])
def delete_event(id):
    """Delete event"""
    return jsonify({})
