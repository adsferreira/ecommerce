from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.user import User
from app.services.customer_order_service import CustomerOrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/routes/orders', methods=['GET'])
def get_all_orders():
    """Retrieve all customer orders."""
    orders = CustomerOrderService.get_all_orders()
    return jsonify([order.as_dict() for order in orders]), 200

@order_bp.route('/routes/orders/<int:ord_id>', methods=['GET'])
@jwt_required()
def get_order_by_id(ord_id):
    """Retrieve a customer order by its ID."""
    order = CustomerOrderService.get_order_by_id(ord_id)
    if order:
        return jsonify(order.as_dict()), 200
    return jsonify({'message': 'Order not found'}), 404

@order_bp.route('/routes/orders', methods=['POST'])
@jwt_required()
def place_order():
    """Place a new order for the logged-in customer."""
    user_id = get_jwt_identity()  # Get the logged-in user's ID from the JWT token
    user = User.query.get(user_id)

    if not user or user.customer is None:
        return jsonify({'message': 'Customer not found'}), 404

    customer_id = user.customer.cusId  # Retrieve the customer's ID from the user relationship
    order_data = request.json  # Get JSON data from the request
    result, status_code = CustomerOrderService.place_order(customer_id, order_data)  # Use service layer
    order_data = {}  # Clear the order data after processing
    return jsonify(result), status_code  # Return the result and appropriate status code

@order_bp.route('/routes/orders/<int:ord_id>', methods=['PUT'])
@jwt_required()
def update_order(ord_id):
    """Update an existing customer order."""
    data = request.json
    order = CustomerOrderService.update_order(ord_id, data)
    if order:
        return jsonify(order.as_dict()), 200
    return jsonify({'message': 'Order not found'}), 404

@order_bp.route('/routes/orders/<int:ord_id>', methods=['DELETE'])
@jwt_required()
def delete_order(ord_id):
    """Delete a customer order."""
    order = CustomerOrderService.delete_order(ord_id)
    if order:
        return jsonify({'message': 'Order deleted'}), 200
    return jsonify({'message': 'Order not found'}), 404
