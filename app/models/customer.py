from app import db

class Customer(db.Model):
    """
    Represents the 'customer' table in the database.

    Attributes:
        cusId (int): Primary key, unique identifier for each customer.
        cusFirstName (str): The first name of the customer, cannot be null.
        cusLastName (str): The last name of the customer, cannot be null.
        cusEmail (str): The email address of the customer, cannot be null.
        cusAddress (str): The physical address of the customer, cannot be null.
        cusCity (str): The city of the customer's address, cannot be null.
        cusState (str): The state of the customer's address, cannot be null.
        cusCountry (str): The country of the customer's address, cannot be null.
        cusPostalCode (str): The postal code of the customer's address, cannot be null.
        cusPhoneNumber (str): The phone number of the customer, can be null.

    Relationships:
        orders: One-to-Many relationship with the CustomerOrder model.
                This allows for retrieving all orders made by a customer.
    """
    __tablename__ = 'customer'

    cusId = db.Column(db.Integer, primary_key=True)
    cusFirstName = db.Column(db.String, nullable=False)
    cusLastName = db.Column(db.String, nullable=False)
    cusEmail = db.Column(db.String, nullable=False)
    cusAddress = db.Column(db.String, nullable=False)
    cusCity = db.Column(db.String, nullable=False)
    cusState = db.Column(db.String, nullable=False)
    cusCountry = db.Column(db.String, nullable=False)
    cusPostalCode = db.Column(db.String, nullable=False)
    cusPhoneNumber = db.Column(db.String)

    # Establish relationship to CustomerOrder
    orders = db.relationship('CustomerOrder', backref='customer', lazy=True)
