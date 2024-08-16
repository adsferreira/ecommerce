from flask import Blueprint, request, jsonify
from app.services.department_service import DepartmentService

department_bp = Blueprint('department', __name__)

@department_bp.route('/routes/departments', methods=['GET'])
def get_all_departments():
    """Retrieve all departments."""
    departments = DepartmentService.get_all_departments()
    return jsonify([department.as_dict() for department in departments]), 200

@department_bp.route('/routes/departments/<int:depId>', methods=['GET'])
def get_department_by_id(dep_id):
    """Retrieve a department by its ID."""
    department = DepartmentService.get_department_by_id(dep_id)
    if department:
        return jsonify(department.as_dict()), 200
    return jsonify({'message': 'Department not found'}), 404

@department_bp.route('/routes/departments', methods=['POST'])
def add_department():
    """Add a new department."""
    data = request.json
    department = DepartmentService.add_department(data)
    return jsonify(department.as_dict()), 201

@department_bp.route('/routes/departments/<int:dep_id>', methods=['PUT'])
def update_department(dep_id):
    """Update an existing department."""
    data = request.json
    department = DepartmentService.update_department(dep_id, data)
    if department:
        return jsonify(department.as_dict()), 200
    return jsonify({'message': 'Department not found'}), 404

@department_bp.route('/routes/departments/<int:dep_id>', methods=['DELETE'])
def delete_department(dep_id):
    """Delete a department."""
    department = DepartmentService.delete_department(dep_id)
    if department:
        return jsonify({'message': 'Department deleted'}), 200
    return jsonify({'message': 'Department not found'}), 404
