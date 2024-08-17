from sqlalchemy.exc import SQLAlchemyError

from app.models.user import User
from app import db


class UserRepository:
    @staticmethod
    def find_by_email(email):
        """
        Find a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The User object if found, else None.
        """
        return User.query.filter_by(usrEmail=email).first()

    @staticmethod
    def find_by_id(user_id):
        """
        Find a user by their ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The User object if found, else None.
        """
        return User.query.get(user_id)

    @staticmethod
    def create_user(data):
        """Create a new user."""
        if not isinstance(data, dict):
            raise TypeError("Data should be a dictionary.")

        try:
            new_user = User(
                usrEmail=data['email'],
                usrFirstName=data['first_name'],
                usrLastName=data['last_name'],
                usrPasswordHash=data['password'],
                usrRole=data.get('role', 'user')  # Default role is 'user'
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def find_by_first_name(first_name):
        return User.query.filter_by(usrFirstName=first_name).first()

    @staticmethod
    def find_by_last_name(last_name):
        return User.query.filter_by(usrLastName=last_name).first()

    @staticmethod
    def find_by_full_name(first_name, last_name):
        return User.query.filter_by(usrFirstName=first_name, usrLastName=last_name).first()

    @staticmethod
    def save(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def update_user(user_id, data):
        """
        Update an existing user.

        Args:
            user_id (int): The ID of the user to be updated.
            data (dict): A dictionary containing the fields to update and their new values.

        Returns:
            tuple: A tuple containing the updated User object and an error message (if any).
        """
        user = UserRepository.find_by_id(user_id)
        if not user:
            return None, "User not found."

        try:
            if 'email' in data:
                user.usrEmail = data['email']
            if 'first_name' in data:
                user.usrFirstName = data['first_name']
            if 'last_name' in data:
                user.usrLastName = data['last_name']
            if 'password' in data:
                user.set_password(data['password'])
            if 'role' in data:
                user.usrRole = data['role']

            db.session.commit()
            return user, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, str(e)
