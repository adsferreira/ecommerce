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
                usrEmail=data.get('usrEmail'),
                usrFirstName=data.get('usrFirstName'),
                usrLastName=data.get('usrLastName'),
                usrPasswordHash=data.get('usrPasswordHash'),
                usrRole=data.get('usrRole')
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

