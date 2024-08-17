import unittest
from app import create_app, db
from app.models.product import Product
from app.services.product_service import ProductService


class ProductServiceTests(unittest.TestCase):
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

    def test_add_product(self):
        response = self.client.post('/routes/products', json={
            'name': 'Test Product',
            'price': 9.99
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product added successfully.', response.json['message'])


if __name__ == '__main__':
    unittest.main()
