from flask import Blueprint, request, jsonify
from app.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/routes/customers', methods=['GET'])
def get_customers():
    """Retrieve all customers."""
    customers = CustomerService.get_all_customers()
    result = [
        {
            'cusId': c.cusId,
            'cusFirstName': c.cusFirstName,
            'cusLastName': c.cusLastName,
            'cusEmail': c.cusEmail,
            'cusAddress': c.cusAddress,
            'cusCity': c.cusCity,
            'cusState': c.cusState,
            'cusCountry': c.cusCountry,
            'cusPostalCode': c.cusPostalCode,
            'cusPhoneNumber': c.cusPhoneNumber
        }
        for c in customers
    ]
    return jsonify(result)

@customer_bp.route('/routes/customers/<int:cusId>', methods=['GET'])
def get_customer(cus_id):
    """Retrieve a single customer by ID."""
    customer = CustomerService.get_customer_by_id(cus_id)
    if customer:
        return jsonify({
            'cusId': customer.cusId,
            'cusFirstName': customer.cusFirstName,
            'cusLastName': customer.cusLastName,
            'cusEmail': customer.cusEmail,
            'cusAddress': customer.cusAddress,
            'cusCity': customer.cusCity,
            'cusState': customer.cusState,
            'cusCountry': customer.cusCountry,
            'cusPostalCode': customer.cusPostalCode,
            'cusPhoneNumber': customer.cusPhoneNumber
        })
    return jsonify({'error': 'Customer not found'}), 404

@customer_bp.route('/routes/customers', methods=['POST'])
def add_customer():
    """Add a new customer."""
    data = request.get_json()
    new_customer = CustomerService.add_customer(data)
    return jsonify({'message': 'Customer added!', 'cusId': new_customer.cusId}), 201

@customer_bp.route('/routes/customers/<int:cusId>', methods=['PUT'])
def update_customer(cus_id):
    """Update an existing customer."""
    data = request.get_json()
    updated_customer = CustomerService.update_customer(cus_id, data)
    if updated_customer:
        return jsonify({'message': 'Customer updated!'})
    return jsonify({'error': 'Customer not found'}), 404

@customer_bp.route('/routes/customers/<int:cusId>', methods=['DELETE'])
def delete_customer(cus_id):
    """Delete a customer."""
    deleted_customer = CustomerService.delete_customer(cus_id)
    if deleted_customer:
        return jsonify({'message': 'Customer deleted!'})
    return jsonify({'error': 'Customer not found'}), 404
