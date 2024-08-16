from app.repositories.department_repository import DepartmentRepository

class DepartmentService:
    """Business logic related to Department."""

    @staticmethod
    def get_all_departments():
        """
        Retrieve all departments.

        Returns:
            list: A list of Department objects.
        """
        return DepartmentRepository.get_all_departments()

    @staticmethod
    def get_department_by_id(dep_id):
        """
        Retrieve a single department by its ID.

        Args:
            dep_id (int): The ID of the department to retrieve.

        Returns:
            Department: A Department object if found, otherwise None.
        """
        return DepartmentRepository.get_department_by_id(dep_id)

    @staticmethod
    def add_department(data):
        """
        Add a new department.

        Args:
            data (dict): A dictionary containing department details. Keys should match the model fields.

        Returns:
            Department: The newly added Department object.
        """
        return DepartmentRepository.add_department(data)

    @staticmethod
    def update_department(dep_id, data):
        """
        Update an existing department.

        Args:
            dep_id (int): The ID of the department to update.
            data (dict): A dictionary containing updated department details. Keys should match the model fields.

        Returns:
            Department: The updated Department object if found and updated, otherwise None.
        """
        return DepartmentRepository.update_department(dep_id, data)

    @staticmethod
    def delete_department(dep_id):
        """
        Delete a department.

        Args:
            dep_id (int): The ID of the department to delete.

        Returns:
            Department: The deleted Department object if found and deleted, otherwise None.
        """
        return DepartmentRepository.delete_department(dep_id)
