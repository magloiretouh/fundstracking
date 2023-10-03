from config import db, login_manager
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from flask_login import UserMixin
from flask import session
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Define the database models
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname_lastname = db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Integer, nullable=True, default=1)
    signature = db.Column(db.LargeBinary, nullable=True)
    signature_filename = db.Column(db.String(100), nullable=True)
    initial = db.Column(db.LargeBinary, nullable=True)
    initial_filename = db.Column(db.String(100), nullable=True)
    user_level_id = db.Column(db.Integer, db.ForeignKey('user_level.id'), nullable=False)
    request_approval_dts = db.relationship('RequestApprovalDatetime', backref='user', lazy=True)

    def __init__(self, username, firstname_lastname, user_level_id):
        self.username = username
        self.firstname_lastname = firstname_lastname
        self.user_level_id = user_level_id

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname_lastname': self.firstname_lastname,
            'user_level_id': self.user_level.serialize(),
        }