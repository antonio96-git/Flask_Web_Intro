# we wanna create database model for both our users and notes
# by doing the aforementioned, we are just SETTING UP the database; we will create it though in __init__.py file

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # foreign key is defined in a "child" model -> ONE TO MANY RELATIONSHIP

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

