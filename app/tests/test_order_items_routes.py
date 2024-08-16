import pytest
from app import create_app, db
from app.models.order_items import OrderItems

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

def test_get_items_by_order(client):
    # Add an order item first
    item = OrderItems(ordId=1, prodId=1, itemQuantity=5, itemPrice=10.00)
    db.session.add(item)
    db.session.commit()

    response = client.get('/api/orders/1/items')
    assert response.status_code == 200
    assert b'5' in response.data

def test_add_item(client):
    data = {
        'ordId': 1,
        'prodId': 1,
        'itemQuantity': 3,
        'itemPrice': 15.00
    }
    response = client.post('/api/orders/1/items', json=data)
    assert response.status_code == 201
    assert b'3' in response.data

def test_update_item(client):
    # Add an order item first
    item = OrderItems(ordId=1, prodId=1, itemQuantity=5, itemPrice=20.00)
    db.session.add(item)
    db.session.commit()

    data = {
        'itemQuantity': 10,
        'itemPrice': 25.00
    }
    response = client.put('/api/orders/1/items/1', json=data)
    assert response.status_code == 200
    assert b'10' in response.data

def test_delete_item(client):
    # Add an order item first
    item = OrderItems(ordId=1, prodId=1, itemQuantity=5, itemPrice=30.00)
    db.session.add(item)
    db.session.commit()

    response = client.delete('/api/orders/1/items/1')
    assert response.status_code == 200
    assert b'Item deleted' in response.data
