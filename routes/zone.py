from config import app
from models import Zone
from flask import Blueprint, jsonify

zone_bp = Blueprint("zone", __name__, url_prefix="/zones")

# Define the zone API routes
@zone_bp.route('/', methods=['GET'])
def get_all_zones():
    zones = Zone.query.all()
    return jsonify([zone.serialize() for zone in zones])

@zone_bp.route('/<int:id>', methods=['GET'])
def get_zone(id):
    zone = Zone.query.filter_by(id=id).first()
    if zone:
        return jsonify(zone.serialize())
    else:
        return jsonify({'error': 'zone not found'}), 404