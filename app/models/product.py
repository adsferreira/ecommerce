from app import db

class Product(db.Model):
    """
    Represents the 'product' table in the database.

    Attributes:
        prodId (int): Primary key, unique identifier for each product.
        prodName (str): The name of the product, cannot be null.
        prodDescription (str): A description of the product, can be null.
        prodPrice (float): The price of the product, cannot be null.
        prodQuantity (int): The available quantity of the product, cannot be null.
        depId (int): Foreign key, references the department the product belongs to.

    Relationships:
        order_items: One-to-Many relationship with the OrderItem model.
                     This allows for retrieving all order items associated with a product.
    """
    __tablename__ = 'product'

    prodId = db.Column(db.Integer, primary_key=True)
    prodName = db.Column(db.String, nullable=False)
    prodDescription = db.Column(db.String)
    prodPrice = db.Column(db.Float, nullable=False)
    prodQuantity = db.Column(db.Integer, nullable=False)
    depId = db.Column(db.Integer, db.ForeignKey('department.depId'), nullable=True)

    # Establish relationship to OrderItem
    order_items = db.relationship('OrderItems', back_populates='product')

    def as_dict(self):
        """Convert the Product model instance to a dictionary."""
        return {
            "prodId": self.prodId,
            "prodName": self.prodName,
            "prodDescription": self.prodDescription,
            "prodPrice": self.prodPrice,
            "prodQuantity": self.prodQuantity,
            "depId": self.depId
        }
