from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class ActivityDomain(db.Model):
    __tablename__ = 'activity_domain'

    id = db.Column(db.Integer, primary_key=True)
    plant = db.Column(db.String(4), nullable=False)
    libelle = db.Column(db.String(255), nullable=False)
    fund_requests = db.relationship('FundRequest', backref='activity_domain', lazy=True)

    def __init__(self, libelle, plant):
        self.libelle = libelle
        self.plant = plant

    def serialize(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'plant': self.plant
        }