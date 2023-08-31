from config import app
from models import CostCenter
from flask import Blueprint, jsonify

cost_center_bp = Blueprint("cost_center", __name__, url_prefix="/cost_centers")

# Define the cost_center API routes
@cost_center_bp.route('/<string:search_term>', methods=['GET'])
def get_search_cost_centers(search_term):
    cost_centers = CostCenter.query.filter(CostCenter.libelle.ilike('%'+search_term+'%'))
    return jsonify([{'cost_center': cost_center.libelle + " ("+ cost_center.code +")", 'id': cost_center.id} for cost_center in cost_centers])