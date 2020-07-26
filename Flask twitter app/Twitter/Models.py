from datetime import datetime

from flask_login import UserMixin

from Twitter import login_manager
from Twitter import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False, default='default.png')
    header = db.Column(db.String(20))
    is_verified = db.Column(db.Boolean, default=0)
    bio = db.Column(db.String(280))
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    following = db.Column(db.Integer, default=0)
    followers = db.Column(db.Integer, default=0)
    tweets = db.relationship('Tweet', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_picture}')"

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Tweet('{self.content}', '{self.date_posted}')"