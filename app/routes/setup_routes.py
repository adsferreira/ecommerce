from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

setup_bp = Blueprint('setup', __name__)

@setup_bp.route('/routes/admin', methods=['POST'])
def setup_admin():
    # Check for setup password
    setup_password = request.headers.get('X-Setup-Password')
    if setup_password != '!@#$':
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')

    if not email or not first_name or not last_name or not password:
        return jsonify({"error": "First and last names, e-mail and password are required."}), 400

    response, status_code = UserService.register_admin(data)
    return jsonify(response), status_code
