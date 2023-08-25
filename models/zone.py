from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class Zone(db.Model):
    __tablename__ = 'zone'

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    fund_requests = db.relationship('FundRequest', backref='zone', lazy=True)

    def __init__(self, libelle):
        self.libelle = libelle

    def serialize(self):
        return {
            'id': self.id,
            'libelle': self.libelle
        }