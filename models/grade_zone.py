from config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Define the database models
class GradeZone(db.Model):
    __tablename__ = 'grade_zone'

    id = db.Column(db.Integer, primary_key=True)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'),nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'),nullable=False)
    montant_perdiem = db.Column(db.Integer, nullable=False)
    montant_logement = db.Column(db.Integer, nullable=False)
    montant_peage = db.Column(db.Integer, nullable=False)

    def __init__(self, grade_id, zone_id, montant_perdiem, montant_logement, montant_peage):
        self.grade_id = grade_id
        self.zone_id = zone_id
        self.montant_perdiem = montant_perdiem
        self.montant_logement = montant_logement
        self.montant_peage = montant_peage

    def serialize(self):
        return {
            'id': self.id,
            'zone_id': self.zone_id,
            'grade_id': self.grade_id,
            'montant_perdiem': self.montant_perdiem,
            'montant_logement': self.montant_logement,
            'montant_peage': self.montant_peage
        }