# app/routes/setup_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import UserService

setup_bp = Blueprint('setup', __name__)

@setup_bp.route('/setup/admin', methods=['POST'])
def setup_admin():
    # Check for setup password
    setup_password = request.headers.get('X-Setup-Password')
    if setup_password != '!@#$':
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    response, status_code = UserService.register_admin(username, password)
    return jsonify(response), status_code
