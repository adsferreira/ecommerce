from app import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(50), nullable=False)  # e.g., 'user' or 'admin'

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password."""
        return check_password_hash(self.password_hash, password)

    def as_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }
