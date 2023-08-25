from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class CostCenter(db.Model):
    __tablename__ = 'cost_center'

    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(12), nullable=False)
    fund_requests = db.relationship('FundRequest', backref='cost_center', lazy=True)

    def __init__(self, libelle, code):
        self.libelle = libelle,
        self.code = code

    def serialize(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'code': self.code
        }