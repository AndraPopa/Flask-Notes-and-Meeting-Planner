import datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(50))
    info = db.Column(db.String(1000))
    when = db.Column(db.DateTime(timezone=True))
    who = db.Column(db.String(50), nullable=True)
    place = db.Column(db.String(50), nullable=True)
    meeting_link = db.Column(db.String(1000), nullable=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(50))
    data = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_birth = db.Column(db.Date)
    notes = db.relationship('Note')
    meetings = db.relationship('Meeting')
