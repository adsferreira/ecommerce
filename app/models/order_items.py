from app import db


class OrderItems(db.Model):
    """
    Represents the 'orderItems' table in the database.

    Attributes:
        ordId (int): Foreign key, references the order this item belongs to. Part of the primary key.
        prodId (int): Foreign key, references the product being ordered. Part of the primary key.
        itemQuantity (int): The quantity of the product ordered, cannot be null.
        itemPrice (float): The price of the product at the time of the order, cannot be null.

    Relationships:
        product: Many-to-One relationship with the Product model.
                 This allows for retrieving the product associated with an order item.
        order: Many-to-One relationship with the CustomerOrder model.
               This allows for retrieving the order associated with an order item.
    """
    __tablename__ = 'orderItems'

    ordId = db.Column(db.Integer, db.ForeignKey('customerOrder.ordId'), primary_key=True)
    prodId = db.Column(db.Integer, db.ForeignKey('product.prodId'), primary_key=True)
    itemQuantity = db.Column(db.Integer, nullable=False)
    itemPrice = db.Column(db.Float, nullable=False)

    # Establish relationships to Product and CustomerOrder
    product = db.relationship('Product',  back_populates='order_items')
    customer_order = db.relationship('CustomerOrder', back_populates='order_items')

    def as_dict(self):
        return {
            'ordId': self.ordId,
            'prodId': self.prodId,
            'itemQuantity': self.itemQuantity,
            'itemPrice': self.itemPrice
        }