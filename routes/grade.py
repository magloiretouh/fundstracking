from config import app
from models import Grade
from flask import Blueprint, jsonify

grade_bp = Blueprint("grade", __name__, url_prefix="/grades")

# Define the zone API routes
@grade_bp.route('/', methods=['GET'])
def get_all_zones():
    grades = Grade.query.all()
    return jsonify([grade.serialize() for grade in grades]), 200

@grade_bp.route('/<int:id>', methods=['GET'])
def get_zone(id):
    grade = Grade.query.filter_by(id=id).first()
    if grade:
        return jsonify(grade.serialize())
    else:
        return jsonify({'error': 'grade not found'}), 404