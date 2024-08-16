from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/routes/products', methods=['GET'])
def get_all_products():
    """Retrieve all products."""
    products = ProductService.get_all_products()
    return jsonify([product.as_dict() for product in products]), 200

@product_bp.route('/routes/products/<int:prod_id>', methods=['GET'])
def get_product_by_id(prod_id):
    """Retrieve a product by its ID."""
    product = ProductService.get_product_by_id(prod_id)
    if product:
        return jsonify(product.as_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/routes/products', methods=['POST'])
def add_product():
    """Add a new product."""
    data = request.json
    product = ProductService.add_product(data)
    return jsonify(product.as_dict()), 201

@product_bp.route('/routes/products/<int:prod_id>', methods=['PUT'])
def update_product(prod_id):
    """Update an existing product."""
    data = request.json
    product = ProductService.update_product(prod_id, data)
    if product:
        return jsonify(product.as_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/routes/products/<int:prod_id>', methods=['DELETE'])
def delete_product(prod_id):
    """Delete a product."""
    product = ProductService.delete_product(prod_id)
    if product:
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'message': 'Product not found'}), 404
