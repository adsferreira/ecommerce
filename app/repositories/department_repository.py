from app import db
from app.models.department import Department

class DepartmentRepository:
    """Handles CRUD operations for Department."""

    @staticmethod
    def get_all_departments():
        """Retrieve all departments."""
        return Department.query.all()

    @staticmethod
    def get_department_by_id(dep_id):
        """Retrieve a single department by ID."""
        return Department.query.get(dep_id)

    @staticmethod
    def add_department(data):
        """
        Add a new department to the database.

        Args:
            data (dict): A dictionary containing department details. Keys should match the model fields.

        Returns:
            Department: The newly added Department object.
            """
        new_department = Department(
            depName=data.get('depName'),
            depDescription=data.get('depDescription')
        )
        db.session.add(new_department)
        db.session.commit()
        return new_department

    @staticmethod
    def update_department(dep_id, data):
        """Update an existing department."""
        department = Department.query.get(dep_id)
        if department:
            department.depName = data.get('depName', department.depName)
            department.depDescription = data.get('depDescription', department.depDescription)
            db.session.commit()
        return department

    @staticmethod
    def delete_department(dep_id):
        """Delete a department."""
        department = Department.query.get(dep_id)
        if department:
            db.session.delete(department)
            db.session.commit()
        return department
