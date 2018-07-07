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

# self links
def get_top_level_links(self, data, many):
    if many:
        self_link = "/users/"
    else:
        self_link = "/users/{}".format(data['id_str'])
        return {'self': self_link}
