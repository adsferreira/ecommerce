from app.repositories.order_items_repository import OrderItemsRepository

class OrderItemsService:
    """Business logic related to OrderItems."""

    @staticmethod
    def get_items_by_order(ord_id):
        """
        Retrieve all items for a specific order.

        Args:
            ord_id (int): The ID of the order for which to retrieve items.

        Returns:
            list: A list of OrderItems objects.
        """
        return OrderItemsRepository.get_items_by_order(ord_id)

    @staticmethod
    def add_item(data):
        """
        Add a new item to an order.

        Args:
            data (dict): A dictionary containing item details. Keys should match the model fields.

        Returns:
            OrderItems: The newly added OrderItems object.
        """
        return OrderItemsRepository.add_item(data)

    @staticmethod
    def update_item(ord_id, prod_id, data):
        """
        Update an existing order item.

        Args:
            ord_id (int): The ID of the order containing the item.
            prod_id (int): The ID of the product for the item.
            data (dict): A dictionary containing updated item details. Keys should match the model fields.

        Returns:
            OrderItems: The updated OrderItems object if found and updated, otherwise None.
        """
        return OrderItemsRepository.update_item(ord_id, prod_id, data)

    @staticmethod
    def delete_item(ord_id, prod_id):
        """
        Delete an order item.

        Args:
            ord_id (int): The ID of the order containing the item.
            prod_id (int): The ID of the product for the item.

        Returns:
            OrderItems: The deleted OrderItems object if found and deleted, otherwise None.
        """
        return OrderItemsRepository.delete_item(ord_id, prod_id)
