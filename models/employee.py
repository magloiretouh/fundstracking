from config import db
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime

# Define the database models
class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    nom_prenoms = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(25), nullable=False)
    fonction = db.Column(db.String(255), nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)

    def __init__(self, nom_prenoms, code, fonction, grade_id):
        self.nom_prenoms = nom_prenoms
        self.code = code
        self.fonction = fonction
        self.grade_id = grade_id

    def serialize(self):
        return {
            'id': self.id,
            'nom_prenoms': self.nom_prenoms,
            'code': self.code,
            'fonction': self.fonction,
            'grade': self.grade.serialize()
        }