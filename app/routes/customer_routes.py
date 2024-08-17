from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.customer_service import CustomerService

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/routes/customers', methods=['GET'])
def get_customers():
    """Retrieve all customers."""
    customers = CustomerService.get_all_customers()
    result = [
        {
            'cusId': c.cusId,
            'cusAddress': c.cusAddress,
            'cusCity': c.cusCity,
            'cusState': c.cusState,
            'cusCountry': c.cusCountry,
            'cusPostalCode': c.cusPostalCode,
            'cusPhoneNumber': c.cusPhoneNumber,
            'usrId': c.usrId
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
            'cusAddress': customer.cusAddress,
            'cusCity': customer.cusCity,
            'cusState': customer.cusState,
            'cusCountry': customer.cusCountry,
            'cusPostalCode': customer.cusPostalCode,
            'cusPhoneNumber': customer.cusPhoneNumber,
            'usrId': customer.usrId
        })
    return jsonify({'error': 'Customer not found'}), 404

@customer_bp.route('/routes/customers', methods=['POST'])
def add_customer():
    """Add a new customer."""
    data = request.get_json()
    new_customer = CustomerService.add_customer(data)
    return jsonify({'message': 'Customer added!', 'cusId': new_customer.cusId}), 201

@customer_bp.route('/routes/customers/me', methods=['PUT'])
@jwt_required()
def update_customer():
    """Update the logged-in user's customer information."""
    # Retrieve user ID from the JWT token
    user_id = get_jwt_identity()
    # Fetch the customer associated with the user
    customer = CustomerService.get_customer_by_user_id(user_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    data = request.get_json()
    updated_customer = CustomerService.update_customer(customer.cusId, data)
    if updated_customer:
        return jsonify({'message': 'Customer updated successfully!'}), 200

    return jsonify({'error': 'Failed to update customer'}), 400

@customer_bp.route('/routes/customers/<int:cusId>', methods=['DELETE'])
def delete_customer(cus_id):
    """Delete a customer."""
    deleted_customer = CustomerService.delete_customer(cus_id)
    if deleted_customer:
        return jsonify({'message': 'Customer deleted!'})
    return jsonify({'error': 'Customer not found'}), 404
