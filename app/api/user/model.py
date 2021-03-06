import mongoengine
from marshmallow import Schema, fields

from app import db
from app.api.list.model import List
from app.api.list.model import ListSchema


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    lists = db.ListField(db.ReferenceField(List, reverse_delete_rule=mongoengine.PULL))
    first_name = db.StringField()
    last_name = db.StringField()

    def __repr__(self):
        return 'ID: {} Email: {}'.format(self.id, self.email)

    def __str__(self):
        return 'id:{}, email:{}'.format(self.id, self.email)


class UserSchema(Schema):
    id = fields.String()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    lists = fields.Nested(ListSchema, many=True, only={'id', 'name', 'archived'})
