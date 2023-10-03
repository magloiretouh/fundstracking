from config import app, db, login_manager, default_password, FIRST_LEVEL, temp_folder
from models import User, UserLevel
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session, send_file
from flask_login import login_user, logout_user, login_required, current_user
from io import BytesIO

user_bp = Blueprint("user", __name__)

# Define the zone API routes

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.form
    user_level = UserLevel.query.filter_by(level=data.get('user_level')).first()

    new_user = User(
        username=data.get('username'), 
        firstname_lastname=data.get('firstname_lastname'),
        user_level_id=user_level.id
    )

    new_user.set_password(data.get('password'))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    user = User.query.filter_by(username=data.get('username')).first()

    if (user and user.check_password(data.get('password')) and data.get('password')==default_password):
        return jsonify({"message": "Redirect To Change Password !"}), 303
    elif (user and user.check_password(data.get('password'))):
        if user.is_active == True:
            login_user(user)
            return jsonify({"message": "Login successfully"}), 200
        else:
            return jsonify({"message": "User is blocked. Please contact the admin !"}), 404
    else:
        return jsonify({"error": "Nom d'utilisateur ou mot de passe erroné !"}), 404


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "You have logged out"}), 200



@user_bp.route('/reset', methods=['POST'])
def reset():
    data = request.form

    user = User.query.filter_by(username=data.get('username')).first()

    if user:
        user.set_password(default_password)
        db.session.commit()
        return jsonify({"message": "User Account reset successfully"}), 200
    else:
        return jsonify({"error": "Invalid username."}), 404


@user_bp.route('/change_password', methods=['POST'])
def change_password():
    data = request.form

    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.check_password(data.get('old_password')):
        if user.is_active == True:
            user.set_password(data.get('new_password'))
            db.session.commit()
            login_user(user)
            return jsonify({"message": "Password changed successfully."}), 200
        else:
            return jsonify({"message": "User is blocked. Please contact the admin !"}), 200
    else:
        return jsonify({"error": "Invalid username or old password."}), 404

@user_bp.route('/current_user')
def get_current_user():
    if current_user.is_authenticated:
        return jsonify(current_user.serialize()), 200
    else:
        return jsonify({'message':'anonymous'}), 204
    
@user_bp.route('/set_signature', methods=['POST'])
@login_required
def set_signature():
    data = request.form
    print(request.files)
    if "signature_file" in request.files and "initial_file" in request.files:
        signature_file = request.files['signature_file']
        initial_file = request.files['initial_file']
    else:
        return jsonify({"message": "Files are not upload."}), 204

    # Save the files in database
    if signature_file and initial_file:
        current_user.signature_filename = signature_file.filename
        current_user.initial_filename = initial_file.filename
        current_user.signature = signature_file.read()
        current_user.initial = initial_file.read()
        db.session.commit()
        return jsonify({"message": "Signature files Saved with success."}), 200


def get_signature(username_id):
    data = request.form
    user = User.query.filter_by(id=username_id).first()
    if user.signature_filename == None:
        return None
    with open(temp_folder+"./"+str(user.id)+user.signature_filename, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(user.signature)
        binary_file.close()
    return temp_folder+"/"+str(user.id)+user.signature_filename

def get_initial(username_id):
    data = request.form
    user = User.query.filter_by(id=username_id).first()
    if user.initial_filename == None:
        return None
    with open(temp_folder+"./"+str(user.id)+user.initial_filename, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(user.initial)
        binary_file.close()
    return temp_folder+"/"+str(user.id)+user.initial_filename


@user_bp.route('/users/<int:level_id>', methods=['GET'])
def get_level_users(level_id):
    users = User.query.filter_by(user_level_id = level_id)
    return jsonify([{"libelle" : user.firstname_lastname, "id" : user.username} for user in users])

@user_bp.route('/users_fl/<string:search_term>', methods=['GET'])
def get_first_level_users(search_term):
    users = User.query.filter(User.firstname_lastname.ilike('%'+search_term+'%'), User.user_level_id==FIRST_LEVEL)
    return jsonify([{'libelle': user.firstname_lastname, "username":user.username} for user in users])