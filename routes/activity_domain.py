from config import app
from models import ActivityDomain
from flask import Blueprint, jsonify

activity_domain_bp = Blueprint("activity_domain", __name__, url_prefix="/activity_domain")

# Define the activity domain API routes
@activity_domain_bp.route('/', methods=['GET'])
def get_all_ad():
    ads = ActivityDomain.query.all()
    return jsonify([ad.serialize() for ad in ads])

@activity_domain_bp.route('/<int:id>', methods=['GET'])
def get_ad(id):
    ad = ActivityDomain.query.filter_by(id=id).first()
    if ad:
        return jsonify(ad.serialize())
    else:
        return jsonify({'error': 'activity domain not found'}), 404