from config import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

# Define the database models
class RequestApprovalDatetime(db.Model):
    __tablename__ = 'request_approval_datetime'

    id = db.Column(db.Integer, primary_key=True)
    fund_request_id = db.Column(db.Integer, db.ForeignKey('fund_request.id'),nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('user_level.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    approved_or_reject = db.Column(db.String(1), nullable=False)

    def __init__(self, fund_request_id, level_id, user_id, approved_or_reject):
        self.fund_request_id = fund_request_id
        self.level_id = level_id
        self.user_id = user_id
        self.approved_or_reject = approved_or_reject

    def serialize(self):
        return {
            'id': self.id,
            'fund_request': self.fund_request.serialize(),
            'level': self.user_level.serialize(),
            'user': self.user.serialize(),
            'approved_or_reject': self.approved_or_reject,
            'created_at': self.created_at
        }