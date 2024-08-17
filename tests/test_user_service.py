import unittest
from app import create_app, db
from app.models.user import User
from app.services.user_service import UserService


class UserServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')  # Use a test config
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_register_user(self):
        response = self.client.post('/register', json={
            'email': 'test.user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully.', response.json['message'])


if __name__ == '__main__':
    unittest.main()
