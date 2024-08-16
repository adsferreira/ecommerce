from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models.customer_order import CustomerOrder
from app.models.order_items import OrderItems


class CustomerOrderRepository:
    """Handles CRUD operations for CustomerOrder."""

    @staticmethod
    def get_all_orders():
        """Retrieve all customer orders."""
        return CustomerOrder.query.all()

    @staticmethod
    def get_order_by_id(ord_id):
        """Retrieve a single customer order by ID."""
        return CustomerOrder.query.get(ord_id)

    @staticmethod
    def place_order(customer_id, order_data):
        """
                Add a new customer order and order items to the database.

                Args:
                    customer_id (int): ID of the customer placing the order.
                    order_data (dict): Dictionary containing order details and items.

                Returns:
                    tuple: (dict, int) - Response message and status code.
                """
        try:
            # Validate order data
            if not order_data.get('items'):
                return {"error": "No items provided for the order."}, 400

            # Create a new customer order
            new_order = CustomerOrder(
                ordDate=order_data.get('ordDate'),
                ordFreight=order_data.get('ordFreight'),
                ordTax=order_data.get('ordTax'),
                cusId=customer_id
            )
            db.session.add(new_order)
            db.session.flush()  # Ensure the order ID is generated before adding order items

            # Add order items
            for item in order_data.get('items', []):
                if not all(k in item for k in ('prodId', 'itemQuantity', 'itemPrice')):
                    return {"error": "Missing item details."}, 400
                order_item = OrderItems(
                    ordId=new_order.ordId,
                    prodId=item.get('prodId'),
                    itemQuantity=item.get('itemQuantity'),
                    itemPrice=item.get('itemPrice')
                )
                db.session.add(order_item)

            db.session.commit()
            return {
                "ordId": new_order.ordId,
                "message": "Order placed successfully!"
            }, 201

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_order(ord_id):
        """Delete a customer order."""
        order = CustomerOrder.query.get(ord_id)
        if order:
            db.session.delete(order)
            db.session.commit()
        return order

    @staticmethod
    def update_order(ord_id, data):
        """Update an existing customer order."""
        order = CustomerOrder.query.get(ord_id)
        if order:
            order.ordDate = data.get('ordDate', order.ordDate)
            order.ordFreight = data.get('ordFreight', order.ordFreight)
            order.ordTax = data.get('ordTax', order.ordTax)
            order.cusId = data.get('cusId', order.cusId)
            db.session.commit()
        return order
