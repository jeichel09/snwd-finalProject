from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ninja_messenger import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    #return User.query.get(int(user_id))
    return db.session.query(User).get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, unique=False)
    messages = db.relationship('Message', backref='author', lazy='dynamic')
    session_token = db.Column(db.String, unique=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(20), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)