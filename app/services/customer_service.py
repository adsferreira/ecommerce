from app.repositories.customer_repository import CustomerRepository

class CustomerService:
    """Business logic related to Customer."""

    @staticmethod
    def get_all_customers():
        return CustomerRepository.get_all_customers()

    @staticmethod
    def get_customer_by_id(cus_id):
        return CustomerRepository.get_customer_by_id(cus_id)

    @staticmethod
    def add_customer(data):
        return CustomerRepository.add_customer(data)

    @staticmethod
    def update_customer(cus_id, data):
        return CustomerRepository.update_customer(cus_id, data)

    @staticmethod
    def delete_customer(cus_id):
        return CustomerRepository.delete_customer(cus_id)
