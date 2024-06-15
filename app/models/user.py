from mongoengine import Document, StringField, DateField, BinaryField, ReferenceField, ListField, EmbeddedDocumentField

from app.models.country import Country


class User(Document):
    username = StringField(primary_key=True)
    first_name = StringField(db_field="firstName", max_length=70, required=True)
    last_name = StringField(db_field="lastName", max_length=70)
    gender = StringField(db_field="gender", max_length=1)
    email = StringField(db_field="email", max_length=100, required=True)
    date_of_birth = DateField(db_field="dateOfBirth", required=True)
    icon = BinaryField
    country = EmbeddedDocumentField(Country, required=True)
    followers = ListField(ReferenceField('self'))
    following = ListField(ReferenceField('self'))
