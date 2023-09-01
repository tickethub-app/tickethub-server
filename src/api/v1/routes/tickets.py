from flask import jsonify, abort, request
from models import storage
from models.ticket import Ticket
from api.v1.routes import app_routes

@app_routes.route("/tickets", strict_slashes=False)
def all_tickets():
    """Get all tickets"""
    all_tickets = storage.all(Ticket)
    formated = [ticket.to_dict() for ticket in all_tickets]
    return jsonify({"status": "success", "data": formated})

@app_routes.route("/tickets/<ticket_id>", strict_slashes=False)
def get_ticket(ticket_id):
  """Get specific ticket"""
  ticket = storage.get(Ticket, ticket_id)
  if ticket is None:
     abort(404)
  return jsonify({"status": "success", "data": ticket.to_dict()})

@app_routes.route("/tickets", methods=["POST"], strict_slashes=False)
def create_ticket():
   """Creates a new ticket"""
   request_data = request.get_json()
   if request_data is None:
      return jsonify({"status": "error", "message": "No data sent"}), 400
   new_ticket = Ticket(**request_data)
   new_ticket.save()
   return jsonify({"status": "success", "data": new_ticket.to_dict()}), 201

@app_routes.route("/tickets/<ticket_id>", methods=["PUT"], strict_slashes=False)
def update_ticket(ticket_id):
   """Updates a ticket"""
   ticket = storage.get(Ticket, ticket_id)
   if ticket is None:
      abort(404)
   data = request.get_json()
   if data is None:
      return jsonify({"status": "error", "message": "No data sent"}), 400
   ignore =  ["event_id"]
   for key, value in data.items():
      if key not in ignore:
        setattr(ticket, key, value)
   ticket.save()
   return jsonify({"status": "success", "message":"ticket updated with success", "data": ticket.to_dict()})


@app_routes.route("/tickets/<ticket_id>", methods=["DELETE"], strict_slashes=False)
def delete_ticket(ticket_id):
   """Delete a ticket"""
   ticket = storage.get(Ticket, ticket_id)
   if ticket is None:
      abort(404)
   ticket.delete()
   return jsonify({"status": "success", "message": "Ticket removed with success!"})