from app import db

class Customer(db.Model):
    """
    Represents the 'customer' table in the database.

    Attributes:
        cusId (int): Primary key, unique identifier for each customer.
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
    cusAddress = db.Column(db.String(64), nullable=False)
    cusCity = db.Column(db.String(32), nullable=False)
    cusState = db.Column(db.String(32), nullable=False)
    cusCountry = db.Column(db.String(32), nullable=False)
    cusPostalCode = db.Column(db.String(16), nullable=False)
    cusPhoneNumber = db.Column(db.String(16))
    usrId = db.Column(db.Integer, db.ForeignKey('user.usrId'), nullable=False)

    # Establish relationship to CustomerOrder
    orders = db.relationship('CustomerOrder', backref='customer', lazy=True)
    user = db.relationship('User', back_populates='customers')
