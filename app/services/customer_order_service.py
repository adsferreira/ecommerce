from datetime import datetime
from app.repositories.customer_order_repository import CustomerOrderRepository

class CustomerOrderService:
    """Business logic related to CustomerOrder."""

    @staticmethod
    def get_all_orders():
        """
        Retrieve all customer orders.

        Returns:
            list: A list of CustomerOrder objects.
        """
        return CustomerOrderRepository.get_all_orders()

    @staticmethod
    def get_orders_by_user(user_id):
        """Retrieve all orders for the given user_id."""
        return CustomerOrderRepository.get_orders_by_user(user_id)

    @staticmethod
    def get_order_by_id(ord_id):
        """
        Retrieve a single customer order by its ID.

        Args:
            ord_id (int): The ID of the order to retrieve.

        Returns:
            CustomerOrder: A CustomerOrder object if found, otherwise None.
        """
        return CustomerOrderRepository.get_order_by_id(ord_id)

    @staticmethod
    def update_order(ord_id, data):
        """
        Update an existing customer order.

        Args:
            ord_id (int): The ID of the order to update.
            data (dict): A dictionary containing updated order details. Keys should match the model fields.

        Returns:
            CustomerOrder: The updated CustomerOrder object if found and updated, otherwise None.
        """
        return CustomerOrderRepository.update_order(ord_id, data)

    @staticmethod
    def delete_order(ord_id):
        """
        Delete a customer order.

        Args:
            ord_id (int): The ID of the order to delete.

        Returns:
            CustomerOrder: The deleted CustomerOrder object if found and deleted, otherwise None.
        """
        return CustomerOrderRepository.delete_order(ord_id)

    @staticmethod
    def place_order(customer_id, order_data):
        """
        Place an order for a customer by delegating the task to the repository.

        Args:
            customer_id (int): ID of the customer placing the order.
            order_data (dict): Dictionary containing order details and items.

        Returns:
            dict: Information about the placed order or error message.
        """
        # Convert ordDate to a Python date object
        try:
            ord_date_str = order_data.get('order_date')
            if ord_date_str:
                ord_date = datetime.strptime(ord_date_str, '%Y-%m-%d').date()
            else:
                ord_date = None
        except ValueError:
            return {"error": "Invalid date format. Use YYYY-MM-DD."}, 400

        # Update order data with the converted date
        order_data['order_date'] = ord_date

        # Call the repository to handle database operations
        return CustomerOrderRepository.place_order(customer_id, order_data)
