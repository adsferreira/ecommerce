from app.repositories.product_repository import ProductRepository

class ProductService:
    """Business logic related to Product."""

    @staticmethod
    def get_all_products():
        """
        Retrieve all products.

        Returns:
            list: A list of Product objects.
        """
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(prod_id):
        """
        Retrieve a single product by its ID.

        Args:
            prod_id (int): The ID of the product to retrieve.

        Returns:
            Product: A Product object if found, otherwise None.
        """
        return ProductRepository.get_product_by_id(prod_id)

    @staticmethod
    def add_product(data):
        """
        Add a new product.

        Args:
            data (dict): A dictionary containing product details. Keys should match the model fields.

        Returns:
            Product: The newly added Product object.
        """
        return ProductRepository.add_product(data)

    @staticmethod
    def update_product(prod_id, data):
        """
        Update an existing product.

        Args:
            prod_id (int): The ID of the product to update.
            data (dict): A dictionary containing updated product details. Keys should match the model fields.

        Returns:
            Product: The updated Product object if found and updated, otherwise None.
        """
        return ProductRepository.update_product(prod_id, data)

    @staticmethod
    def delete_product(prod_id):
        """
        Delete a product.

        Args:
            prod_id (int): The ID of the product to delete.

        Returns:
            Product: The deleted Product object if found and deleted, otherwise None.
        """
        return ProductRepository.delete_product(prod_id)
