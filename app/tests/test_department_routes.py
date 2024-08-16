import pytest
from app import create_app, db
from app.models.department import Department

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

def test_get_all_departments(client):
    response = client.get('/api/departments')
    assert response.status_code == 200
    assert b'[]' in response.data  # Assuming the database is empty

def test_add_department(client):
    data = {
        'depName': 'Electronics',
        'depDescription': 'Devices and gadgets'
    }
    response = client.post('/api/departments', json=data)
    assert response.status_code == 201
    assert b'Electronics' in response.data

def test_get_department_by_id(client):
    # Add a department first
    department = Department(depName='Furniture', depDescription='Home furnishings')
    db.session.add(department)
    db.session.commit()

    response = client.get(f'/api/departments/{department.depId}')
    assert response.status_code == 200
    assert b'Furniture' in response.data

def test_update_department(client):
    # Add a department first
    department = Department(depName='Toys', depDescription='Children’s toys')
    db.session.add(department)
    db.session.commit()

    data = {
        'depName': 'Kids',
        'depDescription': 'Toys and games for children'
    }
    response = client.put(f'/api/departments/{department.depId}', json=data)
    assert response.status_code == 200
    assert b'Kids' in response.data

def test_delete_department(client):
    # Add a department first
    department = Department(depName='Books', depDescription='Books and literature')
    db.session.add(department)
    db.session.commit()

    response = client.delete(f'/api/departments/{department.depId}')
    assert response.status_code == 200
    assert b'Department deleted' in response.data
