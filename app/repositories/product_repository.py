from app import db
from app.models.product import Product

class ProductRepository:
    """Handles CRUD operations for Product."""

    @staticmethod
    def get_all_products():
        """Retrieve all products."""
        return Product.query.all()

    @staticmethod
    def get_product_by_id(prod_id):
        """Retrieve a single product by ID."""
        return Product.query.get(prod_id)

    @staticmethod
    def add_product(data):
        """
        Add a new product to the database.

        Args:
            data (dict): A dictionary containing product details. Keys should match the model fields.

        Returns:
            Product: The newly added Product object.
        """
        new_product = Product(
            prodName=data.get('prodName'),
            prodDescription=data.get('prodDescription'),
            prodPrice=data.get('prodPrice'),
            prodQuantity=data.get('prodQuantity'),
            depId=data.get('depId')
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update_product(prod_id, data):
        """Update an existing product."""
        product = Product.query.get(prod_id)
        if product:
            product.prodName = data.get('prodName', product.prodName)
            product.prodDescription = data.get('prodDescription', product.prodDescription)
            product.prodPrice = data.get('prodPrice', product.prodPrice)
            product.prodQuantity = data.get('prodQuantity', product.prodQuantity)
            product.depId = data.get('depId', product.depId)
            db.session.commit()
        return product

    @staticmethod
    def delete_product(prod_id):
        """Delete a product."""
        product = Product.query.get(prod_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
