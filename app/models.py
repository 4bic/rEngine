from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id_str = db.Column(db.Text, nullable=False)
    created = db.Column(db.Timestamp, nullable=False)
    description = db.Column(db.Text, nullable=True)
    text = db.Column(db.Text, nullable=False)
    user_created = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __init__(self,created,name, text,description):
        self.created = created
        self.name = name
        self.text = text
        self.description = description

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

class UsersSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    id_str = fields.String(dump_only=True)
    name = fields.String(validate=not_blank)
    created = fields.LocalDateTime(validate=not_blank)
    text = fields.String(required=True)


# self links
def get_top_level_links(self, data, many):
    if many:
        self_link = "/users/"
    else:
        self_link = "/users/{}".format(data['id_str'])
        return {'self': self_link}
 #The below type object is a resource identifier object as per http://jsonapi.org/format/#document-resource-identifier-objects
 class Meta:
     type_ = 'users'
