from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField, BinaryField, \
    EmbeddedDocumentField

from app.models.country import Country
from app.models.user import User


class Trip(Document):
    name = StringField(max_length=70, required=True)
    start_date= DateTimeField(db_field="startDate", required=True)
    end_date= DateTimeField(db_field="endDate", required=True)
    users = ListField(ReferenceField(User))
    image = BinaryField
    countries = ListField(EmbeddedDocumentField(Country), required=True)
