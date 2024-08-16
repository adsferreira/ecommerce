from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'user'

    usrId = Column(db.Integer, primary_key=True)
    usrEmail = db.Column(db.String(120), unique=True, nullable=False)
    usrFirstName = db.Column(db.String(64), nullable=False)
    usrLastName = db.Column(db.String(64), nullable=False)
    usrPasswordHash = Column(db.String(128), nullable=False)
    usrRole = Column(db.String(50), nullable=False)  # e.g., 'user' or 'admin'

    def set_password(self, password):
        """Hash and set the user's password."""
        self.usrPasswordHash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password."""
        return check_password_hash(self.usrPasswordHash, password)

    def as_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'usrId': self.id,
            'usrEmail': self.name,
            'usrFirstName': self.usrFirstName,
            'usrLastName': self.usrLastName,
            'usrPasswordHash': self.usrPasswordHash,
            'usrRole': self.usrRole
        }
