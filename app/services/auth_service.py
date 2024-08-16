from app.models.user import User
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthService:
    @staticmethod
    def register_user(data):
        """
        Register a new user.

        Args:
            data (dict): A dictionary containing user details.

        Returns:
            dict: Registration result or error message.
        """
        if UserRepository.find_by_email(data['email']):
            return {"error": "Email already in use."}, 400

        hashed_password = generate_password_hash(data['password'])
        data['password'] = hashed_password
        user = UserRepository.create_user(data)
        return {
            "message": "User registered successfully!",
            "user_id": user.id
        }, 201

    @staticmethod
    def login_user(data):
        """
        Authenticate and log in a user.

        Args:
            data (dict): A dictionary containing email and password.

        Returns:
            dict: Access and refresh tokens, or error message.
        """
        user = UserRepository.find_by_email(data['email'])
        if not user or not check_password_hash(user.password, data['password']):
            return {"error": "Invalid credentials."}, 401

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 200

    @staticmethod
    def get_user(user_id):
        """
        Retrieve a user's details.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict: User details or error message.
        """
        user = UserRepository.find_by_id(user_id)
        if not user:
            return {"error": "User not found."}, 404

        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role
        }, 200

    @staticmethod
    def register_admin(data):
        """Register a new admin user."""
        # Check if the username already exists
        if UserRepository.find_by_username(data['username']):
            return {"error": "Username already exists."}, 400

        # Create a new admin user
        new_admin = User(
            username=data['username'],
            role='admin'
        )
        new_admin.set_password(data['password'])

        # Save the new admin
        saved_admin, error = UserRepository.save(new_admin)
        if error:
            return {"error": error}, 500

        return {
            "message": "Admin registered successfully.",
            "admin": saved_admin.as_dict()
        }, 201
