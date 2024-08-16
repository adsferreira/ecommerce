from app import db
from datetime import datetime


class CustomerOrder(db.Model):
    """
    Represents the 'customerOrder' table in the database.

    Attributes:
        ordId (int): Primary key, unique identifier for each order.
        ordDate (date): The date the order was placed, cannot be null.
        ordFreight (float): The freight cost associated with the order, can be null.
        ordTax (float): The tax associated with the order, can be null.
        cusId (int): Foreign key, references the customer who placed the order.

    Relationships:
        order_items: One-to-Many relationship with the OrderItem model.
                     This allows for retrieving all items associated with an order.
    """
    __tablename__ = 'customerOrder'

    ordId = db.Column(db.Integer, primary_key=True)
    ordDate = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    ordFreight = db.Column(db.Float)
    ordTax = db.Column(db.Float)
    cusId = db.Column(db.Integer, db.ForeignKey('customer.cusId'), nullable=True)

    # Establish relationship to OrderItem
    order_items = db.relationship('OrderItems', back_populates='customer_order')

    def as_dict(self):
        return {
            'ordId': self.ordId,
            'ordDate': self.ordDate.strftime('%Y-%m-%d') if self.ordDate else None,
            'ordFreight': self.ordFreight,
            'ordTax': self.ordTax,
            'cusId': self.cusId
        }
