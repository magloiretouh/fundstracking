from config import app
from models import UserLevel
from flask import Blueprint, jsonify

level_bp = Blueprint("level", __name__, url_prefix="/levels")

# Define the zone API routes
@level_bp.route('/', methods=['GET'])
def get_all_levels():
    levels = UserLevel.query.order_by(UserLevel.level.asc()).all()
    return jsonify({'levels':[level.serialize() for level in levels]}), 200

@level_bp.route('/<int:id>', methods=['GET'])
def get_level(id):
    level = UserLevel.query.filter_by(id=id).first()
    if level:
        return jsonify(level.serialize())
    else:
        return jsonify({'error': 'level not found'}), 404