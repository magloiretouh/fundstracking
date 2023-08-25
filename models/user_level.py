from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class UserLevel(db.Model):
    __tablename__ = 'user_level'

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(2), nullable=False)
    users = db.relationship('User', backref='user_level', lazy=True)
    request_approval_dts = db.relationship('RequestApprovalDatetime', backref='user_level', lazy=True)

    # def __init__(self, libelle, level):
    #     self.libelle = libelle
    #     self.level = level

    def serialize(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'level': self.level
        }