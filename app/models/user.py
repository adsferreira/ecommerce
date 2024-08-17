from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    """
        Represents the 'user' table in the database.

        Attributes:
            usrId (int): Primary key, unique identifier for each user.
            usrEmail (str): Email address of the user, must be unique and cannot be null.
            usrFirstName (str): User's first name, cannot be null.
            usrLastName (str): User's last name, cannot be null.
            usrPasswordHash (str): Hashed password of the user, cannot be null.
            usrRole (str): Role of the user, e.g., 'user' or 'admin', cannot be null.

        Relationships:
            customer: One-to-One relationship with the Customer model.
                      This allows retrieving the customer information associated with the user.
        """
    __tablename__ = 'user'

    usrId = Column(db.Integer, primary_key=True)
    usrEmail = db.Column(db.String(128), unique=True, nullable=False)
    usrFirstName = db.Column(db.String(64), nullable=False)
    usrLastName = db.Column(db.String(64), nullable=False)
    usrPasswordHash = Column(db.String(128), nullable=False)
    usrRole = Column(db.String(32), nullable=False)  # e.g., 'user' or 'admin'

    customer = db.relationship('Customer', back_populates='user', uselist=False)

    def set_password(self, password):
        """
                Hash and set the user's password.

                Args:
                    password (str): The password to hash and set.
                """
        self.usrPasswordHash = generate_password_hash(password)

    def check_password(self, password):
        """
               Check the hashed password against the provided password.

               Args:
                   password (str): The password to check.

               Returns:
                   bool: True if the password matches, False otherwise.
               """
        return check_password_hash(self.usrPasswordHash, password)

    def as_dict(self):
        """
               Convert the User object to a dictionary.

               Returns:
                   dict: A dictionary representation of the User object.
               """
        return {
            'usrId': self.usrId,
            'usrEmail': self.usrEmail,
            'usrFirstName': self.usrFirstName,
            'usrLastName': self.usrLastName,
            'usrPasswordHash': self.usrPasswordHash,
            'usrRole': self.usrRole
        }
