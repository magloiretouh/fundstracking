from config import app, db, upload_folder, LAST_LEVEL, FIRST_LEVEL, COMPLETED_STATUS, REJECTED_STATUS, fr_template_file_path, generate_fr_folder
from models import FundRequest, EmployeeRequest, Employee, GradeZone, RequestApprovalDatetime
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, request, send_file
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from docxtpl import DocxTemplate
from num2words import num2words
import uuid
import os

fund_request_bp = Blueprint("fund_request", __name__, url_prefix="/fund_requests")

# Define the fund_request API routes
@fund_request_bp.route("/", methods=["POST"])
def create_fund_request():
    data = request.form

    # Extract data from request form and create a new FundRequest instance
    new_fund_request = FundRequest(
        itineraire=data.get('itineraire'),
        moyen_de_transport=data.get('moyen_de_transport'),
        zone_id=data.get('zone_id'),
        but_de_la_mission=data.get('but_de_la_mission'),
        date_debut=data.get('date_debut'),
        date_fin=data.get('date_fin'),
        domaine_activite_id=data.get('domaine_activite_id'),
        centre_de_cout_id=data.get('centre_de_cout_id'),
        nom_prenoms_chauffeur=data.get('nom_prenoms_chauffeur')
    )

    # Save the Fund Request Transaction
    db.session.add(new_fund_request)
    db.session.commit()
    new_fund_request.request_track_id = "TGNSCT"+str(new_fund_request.id).zfill(7)

    # Save the relations between the employees and the fund request

    employee_ids = data.get('participants').split(";")
    for employee_id in employee_ids:
        grade_id = Employee.query.get(employee_id).grade.id
        grade_zone = GradeZone.query.filter_by(grade_id = grade_id, zone_id = data.get('zone_id')).first()
        perdiem = grade_zone.montant_perdiem
        logement = grade_zone.montant_logement
        peage = grade_zone.montant_peage

        db.session.add(EmployeeRequest(
            fund_request_id=new_fund_request.id,
            employee_id=employee_id,
            montant_perdiem = perdiem * ((datetime.strptime(data.get('date_fin'), '%Y-%m-%d') - datetime.strptime(data.get('date_debut'), '%Y-%m-%d')).days+0.5),
            montant_logement = logement * ((datetime.strptime(data.get('date_fin'), '%Y-%m-%d') - datetime.strptime(data.get('date_debut'), '%Y-%m-%d')).days),
            montant_peage = peage
        ))

    db.session.commit()

    return jsonify({"message": "Fund request created successfully"}), 201


@fund_request_bp.route("/<int:request_id>", methods=["GET"])
@login_required
def get_fund_request(request_id):
    fund_request = FundRequest.query.get(request_id)

    if fund_request is None:
        return jsonify({"error": "Fund request not found"}), 404

    employee_ids = [employee_request.employee_id for employee_request in EmployeeRequest.query.filter_by(fund_request_id=request_id).all()]

    if employee_ids is None:
        return jsonify({"error": "Employees related to fund request not found"}), 404

    # Query the database to retrieve employees based on the list of IDs
    employees = Employee.query.filter(Employee.id.in_(employee_ids)).all()

    serialized_employees = []

    for employee in employees:
        emp_req = EmployeeRequest.query.filter_by(employee_id = employee.id, fund_request_id = request_id).first()
        emp_json = employee.serialize()
        emp_json['montant_perdiem'] = emp_req.montant_perdiem
        emp_json['montant_logement'] = emp_req.montant_logement
        emp_json['montant_peage'] = emp_req.montant_peage
        serialized_employees.append(emp_json)

    return jsonify(fund_request = fund_request.serialize(), employees = serialized_employees), 200


@fund_request_bp.route("/", methods=["GET"])
@login_required
def get_all_fund_request():
    fund_requests = FundRequest.query.filter_by(approval_level=current_user.user_level.level)

    if fund_requests.first() is None:
        return jsonify({"message": "No Funds request found."}), 200

    fund_requests_serialized = [fund_request.serialize() for fund_request in fund_requests]

    return jsonify(fund_requests_serialized), 200


@fund_request_bp.route("/approve", methods=["POST"])
@login_required
def approve_fund_request():
    data = request.form

    if "odm_filename" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['odm_filename']

    if file.filename == '' and int(current_user.user_level.level) == FIRST_LEVEL:
        return jsonify({"error": "No selected file"}), 400

    fund_request = FundRequest.query.get(data.get('fund_request_id'))

    if fund_request is None:
        return jsonify({"error": "Fund request not found"}), 404

    if int(current_user.user_level.level) != int(fund_request.approval_level):
        return jsonify({"error": "You're not authorized to approve this request."}), 404

    if int(current_user.user_level.level) == FIRST_LEVEL:
        # Save the file on the server
        if file:
            filename = secure_filename(file.filename)
            fund_request.odm_filename = str(uuid.uuid4()) + '.pdf';
            file_path = os.path.join(upload_folder, fund_request.odm_filename)
            file.save(file_path)

    request_approval_dt = RequestApprovalDatetime(fund_request_id = data.get('fund_request_id'), level_id = current_user.user_level.id, user_id = current_user.id, approved_or_reject = 1)
    db.session.add(request_approval_dt)
    fund_request.approval_level+=1
    if int(current_user.user_level.level) == LAST_LEVEL:
        fund_request.status = COMPLETED_STATUS
    db.session.commit()

    return jsonify({"message": "Fund request approved."}), 200


@fund_request_bp.route("/reject", methods=["POST"])
@login_required
def reject_fund_request():
    data = request.form

    fund_request = FundRequest.query.get(data.get('fund_request_id'))

    if fund_request is None:
        return jsonify({"error": "Fund request not found"}), 404

    if int(current_user.user_level.level) != int(fund_request.approval_level):
        return jsonify({"error": "You're not authorized to reject this request."}), 404        

    request_approval_dt = RequestApprovalDatetime(fund_request_id = data.get('fund_request_id'), level_id = current_user.user_level.id, user_id = current_user.id, approved_or_reject = 0)
    db.session.add(request_approval_dt)
    fund_request.approval_level = REJECTED_STATUS
    fund_request.reject_reason = data.get('reject_reason')
    db.session.commit()

    return jsonify({"message": "Fund request rejected."}), 200


@fund_request_bp.route("/print/<int:request_id>", methods=["GET"])
@login_required
def print_fund_request_(request_id):
    # Get parameters from Fund Request
    fund_request = FundRequest.query.get(request_id)
    duree_mission = (fund_request.date_fin - fund_request.date_debut).days+1

    data = {
        'ITINERAIRE': fund_request.itineraire,
        'BUTDELAMISSION': fund_request.but_de_la_mission,
        'DATEDEDEPART' : fund_request.date_debut.strftime("%d/%m/%Y"),
        'DATEDEFIN': fund_request.date_fin.strftime("%d/%m/%Y"),
        'DUREEMISSION': num2words(duree_mission, lang='fr').capitalize() + ' (' + str(duree_mission) +')',
        'MOYENDETRANSPORT': fund_request.moyen_de_transport,
        'NOMDUCHAUFFEUR': fund_request.nom_prenoms_chauffeur,
        'CENTREDECOUT': fund_request.cost_center.code,
        'NOMAGENTS': '; '.join([Employee.query.get(employee_request.employee_id).nom_prenoms for employee_request in EmployeeRequest.query.filter_by(fund_request_id=request_id).all()]),
        'FONCTIONAGENTS':  '; '.join([Employee.query.get(employee_request.employee_id).fonction for employee_request in EmployeeRequest.query.filter_by(fund_request_id=request_id).all()])
    }

    doc = generate_fr_document(data)
    temp_path = generate_fr_folder + '/' + str(uuid.uuid4()) + '.docx'
    doc.save(temp_path)
    return jsonify({"message": temp_path}), 200

def generate_fr_document(data):
    doc = DocxTemplate(fr_template_file_path)
    doc.render(data)
    return doc