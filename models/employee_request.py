from config import db
from sqlalchemy import Column, Integer, String
from datetime import datetime

# Define the database models
class EmployeeRequest(db.Model):
    __tablename__ = 'employee_request'

    id = db.Column(db.Integer, primary_key=True)
    fund_request_id = db.Column(db.Integer, db.ForeignKey('fund_request.id'),nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),nullable=False)
    montant_perdiem = db.Column(db.Integer, nullable=False)
    montant_logement = db.Column(db.Integer, nullable=False)
    montant_peage = db.Column(db.Integer, nullable=False)

    def __init__(self, fund_request_id, employee_id, montant_perdiem, montant_logement, montant_peage):
        self.fund_request_id = fund_request_id
        self.employee_id = employee_id
        self.montant_perdiem = montant_perdiem
        self.montant_logement = montant_logement
        self.montant_peage = montant_peage

    def serialize(self):
        return {
            'id': self.id,
            'fund_request_id': self.fund_request_id,
            'employee_id': self.employee_id,
            'montant_perdiem': self.montant_perdiem,
            'montant_logement': self.montant_logement,
            'montant_peage': self.montant_peage
        }