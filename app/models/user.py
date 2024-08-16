from app import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)  # e.g., 'user' or 'admin'

    def check_password(self, password):
        return self.password == password  # Simple password check, use hashing in production

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }
