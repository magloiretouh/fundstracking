from config import app
from models import Employee
from flask import Blueprint, jsonify

employee_bp = Blueprint("employee", __name__, url_prefix="/employees")

# Define the employee API routes
@employee_bp.route('/<string:search_term>', methods=['GET'])
def get_search_employees(search_term):
    employees = Employee.query.filter(Employee.nom_prenoms.ilike('%'+search_term+'%'))
    return jsonify([{'id': employee.id, 'full_name': employee.nom_prenoms} for employee in employees])