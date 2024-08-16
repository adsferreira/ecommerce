import pytest
from app import create_app, db
from app.models.customer_order import CustomerOrder

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

def test_get_all_orders(client):
    response = client.get('/api/orders')
    assert response.status_code == 200
    assert b'[]' in response.data  # Assuming the database is empty

def test_add_order(client):
    data = {
        'ordDate': '2024-08-16',
        'ordFreight': 15.00,
        'ordTax': 1.50,
        'cusId': 1
    }
    response = client.post('/api/orders', json=data)
    assert response.status_code == 201
    assert b'2024-08-16' in response.data

def test_get_order_by_id(client):
    # Add an order first
    order = CustomerOrder(ordDate='2024-08-16', ordFreight=10.00, ordTax=2.00, cusId=1)
    db.session.add(order)
    db.session.commit()

    response = client.get(f'/api/orders/{order.ordId}')
    assert response.status_code == 200
    assert b'2024-08-16' in response.data

def test_update_order(client):
    # Add an order first
    order = CustomerOrder(ordDate='2024-08-16', ordFreight=20.00, ordTax=3.00, cusId=1)
    db.session.add(order)
    db.session.commit()

    data = {
        'ordDate': '2024-08-17',
        'ordFreight': 25.00,
        'ordTax': 2.50
    }
    response = client.put(f'/api/orders/{order.ordId}', json=data)
    assert response.status_code == 200
    assert b'2024-08-17' in response.data

def test_delete_order(client):
    # Add an order first
    order = CustomerOrder(ordDate='2024-08-16', ordFreight=30.00, ordTax=5.00, cusId=1)
    db.session.add(order)
    db.session.commit()

    response = client.delete(f'/api/orders/{order.ordId}')
    assert response.status_code == 200
    assert b'Order deleted' in response.data
