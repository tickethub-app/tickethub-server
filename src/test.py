#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.organisation import Organisation
from models.event import Event
from models.ticket import Ticket
from random import randint
from datetime import datetime

organisation = Organisation()
organisation.name = "Ussumane" 
organisation.password = "Test"
organisation.email = "Email" + str(randint(0, 9999))
# organisation.save()

event_dict = {"date": datetime.now(), "start_time": datetime.time(datetime.now()), "end_time": datetime.time(datetime.now()), "number_tickets": 20, "topic": "topico do evento", "description": "description of the event", "organisation_id": "8f7f2fe2-1a1e-4270-a05d-762fd8744c17"}

event = Event(**event_dict)
# print(event.to_dict())
# event.save()
objs = storage.all(Event)
# for obj in objs:
#     print(obj)


ticket_dict = {"attendee_name": "Ussumane Momade", "event_id": objs[0].id, "attended": False}

ticket = Ticket(**ticket_dict)
ticket.save()
print(ticket.to_dict())