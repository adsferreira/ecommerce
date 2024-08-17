from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.user import User
from app import db
from app.services.user_service import UserService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Default to 'user' role

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.as_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = UserService.login_user(data)

    if token:
        return jsonify(token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    response, status_code = UserService.get_user(user_id)
    return jsonify(response), status_code

@auth_bp.route('/register-admin', methods=['POST'])
@jwt_required()
def register_admin():
    """Register a new admin (requires admin privileges)."""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    if current_user.usrRole != 'admin':
        return jsonify({"error": "Admin privileges required."}), 403

    data = request.json
    response, status_code = UserService.register_admin(data)
    return jsonify(response), status_code
