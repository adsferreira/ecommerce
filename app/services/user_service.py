# app/services/user_service.py
from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def register_user(data):
        """Register a new user."""
        if not isinstance(data, dict):
            raise TypeError("Data should be a dictionary.")

        try:
            new_user = UserRepository.create_user(data)
            return {"message": "User registered successfully.", "user": new_user.as_dict()}, 201
        except Exception as e:
            return {"error": str(e)}, 500
