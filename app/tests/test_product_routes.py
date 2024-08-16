import pytest
from app import create_app, db
from app.models.product import Product

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after the test

def test_get_all_products(client):
    response = client.get('/api/products')
    assert response.status_code == 200
    assert b'[]' in response.data  # Assuming the database is empty

def test_add_product(client):
    data = {
        'prodName': 'Test Product',
        'prodDescription': 'A description of the test product',
        'prodPrice': 19.99,
        'prodQuantity': 100
    }
    response = client.post('/api/products', json=data)
    assert response.status_code == 201
    assert b'Test Product' in response.data

def test_get_product_by_id(client):
    # Add a product first
    product = Product(prodName='Sample Product', prodPrice=25.00, prodQuantity=10)
    db.session.add(product)
    db.session.commit()

    response = client.get(f'/api/products/{product.prodId}')
    assert response.status_code == 200
    assert b'Sample Product' in response.data

def test_update_product(client):
    # Add a product first
    product = Product(prodName='Old Name', prodPrice=30.00, prodQuantity=5)
    db.session.add(product)
    db.session.commit()

    data = {
        'prodName': 'Updated Name',
        'prodPrice': 35.00,
        'prodQuantity': 10
    }
    response = client.put(f'/api/products/{product.prodId}', json=data)
    assert response.status_code == 200
    assert b'Updated Name' in response.data

def test_delete_product(client):
    # Add a product first
    product = Product(prodName='Delete Me', prodPrice=50.00, prodQuantity=1)
    db.session.add(product)
    db.session.commit()

    response = client.delete(f'/api/products/{product.prodId}')
    assert response.status_code == 200
    assert b'Product deleted' in response.data
