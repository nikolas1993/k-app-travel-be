from mongoengine import Document, StringField, EmbeddedDocument, DateTimeField, EmbeddedDocumentField, BinaryField, \
    ListField, ReferenceField, IntField

from app.models.trip import Trip
from app.models.user import User


class Departure(EmbeddedDocument):
    airport = StringField(max_length=70, required=True)
    date_time = DateTimeField(db_field="dateTime", required=True)


class Luggages(EmbeddedDocument):
    num_hand_luggages = IntField(db_field="numHandLuggages", min_value=0, required=True)
    num_luggages = IntField(db_field="numLuggages", min_value=0, required=True)
    num_backpack = IntField(db_field="numBackpack", min_value=0, required=True)


class Flight(Document):
    flight_number = StringField(db_field="flightNumber", max_length=70, required=True)
    airline = StringField(max_length=70, required=True)
    departure = EmbeddedDocumentField(Departure, required=True)
    arrival = EmbeddedDocumentField(Departure, required=True)
    terminal = StringField(max_length=70)
    gate = StringField(max_length=70)
    tickets = ListField(BinaryField)
    luggages = EmbeddedDocumentField(Luggages)
    users = ListField(ReferenceField(User))
    trip = ReferenceField(Trip)
