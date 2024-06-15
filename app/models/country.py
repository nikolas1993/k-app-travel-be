from mongoengine import StringField, ListField, EmbeddedDocument, EmbeddedDocumentField


class City(EmbeddedDocument):
    name = StringField(max_length=70, required=True)
    code = StringField(max_length=70, required=True)


class Country(EmbeddedDocument):
    country = StringField(max_length=70, required=True)
    country_code = StringField(db_field="countryCode", max_length=70, required=True)
    cities = ListField(EmbeddedDocumentField(City))
