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
        """
        Create a new user.

        Args:
            data (dict): A dictionary containing user details.

        Returns:
            User: The newly created User object.
        """
        new_user = User(
            email=data['email'],
            password=data['password'],
            name=data['name'],
            role=data['role']  # role could be 'user' or 'admin'
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
