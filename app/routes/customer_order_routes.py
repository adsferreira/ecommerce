from flask import Blueprint, request, jsonify
from app.services.customer_order_service import CustomerOrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/routes/orders', methods=['GET'])
def get_all_orders():
    """Retrieve all customer orders."""
    orders = CustomerOrderService.get_all_orders()
    return jsonify([order.as_dict() for order in orders]), 200

@order_bp.route('/routes/orders/<int:ord_id>', methods=['GET'])
def get_order_by_id(ord_id):
    """Retrieve a customer order by its ID."""
    order = CustomerOrderService.get_order_by_id(ord_id)
    if order:
        return jsonify(order.as_dict()), 200
    return jsonify({'message': 'Order not found'}), 404

@order_bp.route('/routes/orders/<int:customer_id>', methods=['POST'])
def place_order(customer_id):
    """Place a new order for a customer."""
    order_data = request.json  # Get JSON data from the request
    result, status_code = CustomerOrderService.place_order(customer_id, order_data)  # Use service layer
    return jsonify(result), status_code  # Return the result and appropriate status code

@order_bp.route('/routes/orders/<int:ord_id>', methods=['PUT'])
def update_order(ord_id):
    """Update an existing customer order."""
    data = request.json
    order = CustomerOrderService.update_order(ord_id, data)
    if order:
        return jsonify(order.as_dict()), 200
    return jsonify({'message': 'Order not found'}), 404

@order_bp.route('/routes/orders/<int:ord_id>', methods=['DELETE'])
def delete_order(ord_id):
    """Delete a customer order."""
    order = CustomerOrderService.delete_order(ord_id)
    if order:
        return jsonify({'message': 'Order deleted'}), 200
    return jsonify({'message': 'Order not found'}), 404
