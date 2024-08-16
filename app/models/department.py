from app import db


class Department(db.Model):
    """
    Represents the 'department' table in the database.

    Attributes:
        depId (int): Primary key, unique identifier for each department.
        depName (str): The name of the department, cannot be null.
        depDescription (str): A description of the department, can be null.

    Relationships:
        products: One-to-Many relationship with the Product model.
                  This allows for retrieving all products associated with a department.
    """
    __tablename__ = 'department'

    depId = db.Column(db.Integer, primary_key=True)
    depName = db.Column(db.String, nullable=False)
    depDescription = db.Column(db.String)

    # Establish relationship to Product
    products = db.relationship('Product', backref='department', lazy=True)

    def as_dict(self):
        return {
            "depId": self.depId,
            "depName": self.depName,
            "depDescription": self.depDescription
        }