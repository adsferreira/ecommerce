from app import db
from app.models.order_items import OrderItems

class OrderItemsRepository:
    """Handles CRUD operations for OrderItems."""

    @staticmethod
    def get_items_by_order(ord_id):
        """Retrieve all items for a specific order."""
        return OrderItems.query.filter_by(ordId=ord_id).all()

    @staticmethod
    def add_item(data):
        """Add a new item to an order."""
        new_item = OrderItems(
            ordId=data['ordId'],
            prodId=data['prodId'],
            itemQuantity=data['itemQuantity'],
            itemPrice=data['itemPrice']
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def update_item(ord_id, prod_id, data):
        """Update an existing order item."""
        item = OrderItems.query.filter_by(ordId=ord_id, prodId=prod_id).first()
        if item:
            item.itemQuantity = data.get('itemQuantity', item.itemQuantity)
            item.itemPrice = data.get('itemPrice', item.itemPrice)
            db.session.commit()
        return item

    @staticmethod
    def delete_item(ord_id, prod_id):
        """Delete an order item."""
        item = OrderItems.query.filter_by(ordId=ord_id, prodId=prod_id).first()
        if item:
            db.session.delete(item)
            db.session.commit()
        return item
