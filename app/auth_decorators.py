from functools import wraps
from flask import request, jsonify
from app.models.user import User

def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_id = request.headers.get('User-ID')
            if not user_id:
                return jsonify({"error": "User not logged in"}), 403
            user = User.query.get(user_id)
            if not user or user.role != role:
                return jsonify({"error": "Permission denied"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
