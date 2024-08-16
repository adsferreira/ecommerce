from flask import Blueprint, request, jsonify
from app.services.order_items_service import OrderItemsService

order_items_bp = Blueprint('order_items', __name__)

@order_items_bp.route('/routes/orders/<int:ord_id>/items', methods=['GET'])
def get_items_by_order(ord_id):
    """Retrieve all items for a specific order."""
    items = OrderItemsService.get_items_by_order(ord_id)
    return jsonify([item.as_dict() for item in items]), 200

@order_items_bp.route('/routes/orders/<int:ord_id>/items', methods=['POST'])
def add_item():
    """Add a new item to an order."""
    data = request.json
    item = OrderItemsService.add_item(data)
    return jsonify(item.as_dict()), 201

@order_items_bp.route('/routes/orders/<int:ord_id>/items/<int:prod_id>', methods=['PUT'])
def update_item(ord_id, prod_id):
    """Update an existing order item."""
    data = request.json
    item = OrderItemsService.update_item(ord_id, prod_id, data)
    if item:
        return jsonify(item.as_dict()), 200
    return jsonify({'message': 'Item not found'}), 404

@order_items_bp.route('/routes/orders/<int:ord_id>/items/<int:prod_id>', methods=['DELETE'])
def delete_item(ord_id, prod_id):
    """Delete an order item."""
    item = OrderItemsService.delete_item(ord_id, prod_id)
    if item:
        return jsonify({'message': 'Item deleted'}), 200
    return jsonify({'message': 'Item not found'}), 404
