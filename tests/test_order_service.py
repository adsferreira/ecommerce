import unittest
from app import create_app, db
from app.models.order import Order
from app.services.order_service import OrderService


class OrderServiceTests(unittest.TestCase):
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

    def test_place_order(self):
        response = self.client.post('/routes/orders', json={
            'prod_id': 1,
            'quantity': 2,
            'price': 19.98
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order placed successfully.', response.json['message'])


if __name__ == '__main__':
    unittest.main()
