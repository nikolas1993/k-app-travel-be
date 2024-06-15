from mongoengine import Document, StringField, BinaryField, EmbeddedDocument, EmbeddedDocumentField, DateTimeField, \
    IntField, ListField, ReferenceField

from app.models.country import Country
from app.models.trip import Trip
from app.models.user import User


class Address(EmbeddedDocument):
    street = StringField(max_length=70)
    country = EmbeddedDocumentField(Country, required=True)


class BookingInfo(EmbeddedDocument):
    link = StringField(max_length=70)
    booking_number = StringField(db_field="bookingNumber", max_length=70, required=True)
    check_in = DateTimeField(db_field="checkIn", required=True)
    check_out = DateTimeField(db_field="checkOut", required=True)
    num_rooms = IntField(db_field="numRooms", min_value=0, required=True)


class Accomodation(Document):
    name = StringField(db_field="firstName", max_length=70, required=True)
    website = StringField(db_field="firstName", max_length=70)
    image = BinaryField
    address = EmbeddedDocumentField(Address, required=True)
    booking_info = EmbeddedDocumentField(BookingInfo, required=True)
    users = ListField(ReferenceField(User))
    trip = ReferenceField(Trip)
