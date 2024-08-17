from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models.user import User

def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()  # Verifies the JWT in the request
                user_id = get_jwt_identity()  # Extracts the user identity (user_id) from the token
                user = User.query.get(user_id)
                if not user or user.usrRole != role:
                    return jsonify({"error": "Permission denied"}), 403
            except Exception as e:
                return jsonify({"error": "User not logged in", "message": str(e)}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
