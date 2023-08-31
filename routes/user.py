from config import app, db, login_manager, default_password
from models import User
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

user_bp = Blueprint("user", __name__)

# Define the zone API routes

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.form

    new_user = User(
        username=data.get('username'), 
        firstname_lastname=data.get('firstname_lastname'),
        user_level_id=data.get('user_level_id')
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
        login_user(user)
        return jsonify({"message": "Login successfully"}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 404


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
        user.set_password(data.get('new_password'))
        db.session.commit()
        return jsonify({"message": "Password changed successfully."}), 200
    else:
        return jsonify({"error": "Invalid username or old password."}), 404