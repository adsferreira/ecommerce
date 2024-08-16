from app import db
from app.models.customer import Customer

class CustomerRepository:
    """Handles CRUD operations for Customer."""

    @staticmethod
    def get_all_customers():
        """Retrieve all customers."""
        return Customer.query.all()

    @staticmethod
    def get_customer_by_id(cus_id):
        """Retrieve a single customer by ID."""
        return Customer.query.get(cus_id)

    @staticmethod
    def add_customer(data):
        """Add a new customer."""
        new_customer = Customer(
            cusFirstName=data['cusFirstName'],
            cusLastName=data['cusLastName'],
            cusEmail=data['cusEmail'],
            cusAddress=data['cusAddress'],
            cusCity=data['cusCity'],
            cusState=data['cusState'],
            cusCountry=data['cusCountry'],
            cusPostalCode=data['cusPostalCode'],
            cusPhoneNumber=data.get('cusPhoneNumber')
        )
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    @staticmethod
    def update_customer(cus_id, data):
        """Update an existing customer."""
        customer = Customer.query.get(cus_id)
        if customer:
            customer.cusFirstName = data.get('cusFirstName', customer.cusFirstName)
            customer.cusLastName = data.get('cusLastName', customer.cusLastName)
            customer.cusEmail = data.get('cusEmail', customer.cusEmail)
            customer.cusAddress = data.get('cusAddress', customer.cusAddress)
            customer.cusCity = data.get('cusCity', customer.cusCity)
            customer.cusState = data.get('cusState', customer.cusState)
            customer.cusCountry = data.get('cusCountry', customer.cusCountry)
            customer.cusPostalCode = data.get('cusPostalCode', customer.cusPostalCode)
            customer.cusPhoneNumber = data.get('cusPhoneNumber', customer.cusPhoneNumber)
            db.session.commit()
        return customer

    @staticmethod
    def delete_customer(cus_id):
        """Delete a customer."""
        customer = Customer.query.get(cus_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return customer
