import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name,email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

class Results(db.Model):
    __tablename__ = "keywords"
    id = db.Column(db.Integer(),primary_key=True)
    user_name = db.Column(db.String())
    text = db.Column(db.String())
    user_created = db.Column(db.String())

    def __init__(self, name,text,created):
        self.name = user_name
        self.text = text
        self.created = user_created

    def __repr__(self):
        return '<E-mail %r>' % self.email
