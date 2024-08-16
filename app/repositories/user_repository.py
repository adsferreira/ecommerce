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
        return User.query.filter_by(email=email).first()

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
                email=data.get('email'),  # Access dictionary items with .get() method
                password=data.get('password'),
                name=data.get('name'),
                role=data.get('role')
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, str(e)

