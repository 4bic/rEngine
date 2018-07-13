# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import JSON
# import app
# import configparser
#
#
# app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# # Create our database model
# class User(db.Model):
#     __tablename__ = "users"
#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, name,email):
#         self.name = name
#         self.email = email
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
# class Keyword(db.Model):
#     __tablename__ = "keywords"
#     id = db.Column(db.Integer, primary_key=True)
#     search_term = db.Column(db.String, nullable=False)
#
#     def __init__(self, search_term):
#         self.search_term = search_term
#
#     def __repr__(self):
#         return '<search_term {}'.format(self.name)
#
#
# class Results(db.Model):
#     __tablename__ = "tweets_stream"
#     text = Col('text')
#     user_name = Col('user_name')
#     user_location = Col('user_location')
#
#     def __init__(self, search_term):
#         self.search_term = search_term
#
#     def __repr__(self):
#         return '<search_term {}'.format(self.name)
