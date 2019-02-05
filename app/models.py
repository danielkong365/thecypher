from app import db, login
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import backref

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    location = db.Column(db.String(64), index=True)
    sessions = db.relationship('Session', backref='master', lazy='dynamic')
    events = db.relationship('Event', backref='master', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_location_events(self):
        in_location = Event.query.filter(self.location==Event.location).all()
        return in_location
    
    def get_location_sessions(self):
        in_location = Session.query.filter(self.location==Session.location).all()
        return in_location
    

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True)
    address = db.Column(db.String(128), index=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, index=True)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True)
    address = db.Column(db.String(128), index=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date,index=True)
    reoccuring = db.Column(db.Boolean)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))