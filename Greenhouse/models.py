from datetime import datetime
from Greenhouse import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Timer(db.Model):
    tablename = "timer"
    id = db.Column(db.Integer, primary_key=True)
    timerStart = db.Column(db.DateTime(), nullable=False,
                           default=datetime.utcnow)
    timerEnd = db.Column(db.DateTime(), nullable=False,
                         default=datetime.utcnow)
