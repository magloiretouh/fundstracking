from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class Grade(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    employees = db.relationship('Employee', backref='grade', lazy=True)

    def __init__(self, libelle):
        self.libelle = libelle

    def serialize(self):
        return {
            'id': self.id,
            'libelle': self.libelle
        }