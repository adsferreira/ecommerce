import json

import pytest
from app import create_app, db
from app.models.customer import Customer

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after the test

def test_get_all_customers(client):
    response = client.get('/routes/customers')
    assert response.status_code == 200
    assert b'[]' in response.data  # Assuming the database is empty

def test_add_customer(client):
    data = {
        'cusFirstName': 'John',
        'cusLastName': 'Doe',
        'cusEmail': 'john.doe@example.com',
        'cusAddress': '123 Elm St',
        'cusCity': 'Springfield',
        'cusState': 'IL',
        'cusCountry': 'USA',
        'cusPostalCode': '62701',
        'cusPhoneNumber': '555-1234'
    }
    response = client.post('/routes/customers', json=data)

    assert response.status_code == 201

    # Load the response data as JSON
    response_data = json.loads(response.data)

    # Assert the presence of 'cusId' and 'message'
    assert 'cusId' in response_data
    assert response_data['message'] == 'Customer added!'
    assert response_data['cusId'] is not None

def test_get_customer_by_id(client):
    # Add a customer first
    customer = Customer(
        cusFirstName='Jane',
        cusLastName='Smith',
        cusEmail='jane.smith@example.com',
        cusAddress='456 Oak St',
        cusCity='Shelbyville',
        cusState='IL',
        cusCountry='USA',
        cusPostalCode='62565',
        cusPhoneNumber='555-5678'
    )
    db.session.add(customer)
    db.session.commit()

    response = client.get(f'/api/customers/{customer.cusId}')
    assert response.status_code == 200
    assert b'Jane' in response.data

def test_update_customer(client):
    # Add a customer first
    customer = Customer(
        cusFirstName='Alice',
        cusLastName='Johnson',
        cusEmail='alice.johnson@example.com',
        cusAddress='789 Pine St',
        cusCity='Capital City',
        cusState='IL',
        cusCountry='USA',
        cusPostalCode='62704',
        cusPhoneNumber='555-9876'
    )
    db.session.add(customer)
    db.session.commit()

    data = {
        'cusFirstName': 'Alice',
        'cusLastName': 'Doe',
        'cusEmail': 'alice.doe@example.com',
        'cusAddress': '789 Pine St',
        'cusCity': 'Capital City',
        'cusState': 'IL',
        'cusCountry': 'USA',
        'cusPostalCode': '62704',
        'cusPhoneNumber': '555-1234'
    }
    response = client.put(f'/api/customers/{customer.cusId}', json=data)
    assert response.status_code == 200
    assert b'Alice' in response.data

def test_delete_customer(client):
    # Add a customer first
    customer = Customer(
        cusFirstName='Bob',
        cusLastName='Brown',
        cusEmail='bob.brown@example.com',
        cusAddress='321 Birch St',
        cusCity='Metropolis',
        cusState='IL',
        cusCountry='USA',
        cusPostalCode='62960',
        cusPhoneNumber='555-4321'
    )
    db.session.add(customer)
    db.session.commit()

    response = client.delete(f'/api/customers/{customer.cusId}')
    assert response.status_code == 200
    assert b'Customer deleted' in response.data
