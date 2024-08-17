from sqlalchemy.exc import SQLAlchemyError

from app.models.user import User
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token


class UserService:
    @staticmethod
    def register_user(data):
        """
        Register a new user.

        Args:
            data (dict): A dictionary containing user details.

        Returns:
            dict: Registration result or error message.
        """
        if UserRepository.find_by_email(data['usrEmail']):
            return {"error": "Email already in use."}, 400

        hashed_password = generate_password_hash(data['usrPasswordHash'])
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

        if not user or not check_password_hash(user.usrPasswordHash, data['password']):
            return {"error": "Invalid log-in credentials."}, 401

        access_token = create_access_token(identity=user.usrId)
        refresh_token = create_refresh_token(identity=user.usrId)
        return {
            "user": user.as_dict(),
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
            "usrId": user.usrId,
            "usrEmail": user.usrEmail,
            "usrFirstName": user.usrFirstName,
            "usrLastName": user.usrLastName,
            'usrPasswordHash': user.usrPasswordHash,
            "role": user.role
        }, 200

    @staticmethod
    def register_admin(data):
        """Register a new admin user."""
        try:
            email = data.get('email')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            password = data.get('password')
            if UserRepository.find_by_email(email):
                return {"error": "Username already exists."}, 400

            new_admin = User(
                usrEmail=email,
                usrFirstName=first_name,
                usrLastName=last_name,
                usrRole='admin'
            )

            new_admin.set_password(password)
            UserRepository.create_user(new_admin.as_dict())

            return {
                "message": "Admin registered successfully.",
                "admin": new_admin.as_dict()
            }, 201
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500
