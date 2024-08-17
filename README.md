# E-Commerce System

## Overview

This is a Python-based e-commerce system built using Flask. The application features user authentication, product management, and order processing functionalities. The system allows users to register, log in, and place orders. Admins have additional privileges to manage products and oversee the application.

## Features

- **User Authentication**: Register, log in, and manage user accounts.
- **Product Management**: Add, update, and delete products (admin only).
- **Order Processing**: Place and view orders.
- **Role-Based Access Control**: Differentiate between regular users and admin users.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-JWT-Extended**: JWT-based authentication for secure API access.
- **Werkzeug**: For password hashing and checking.
- **SQLite**: Database for development and testing (in-memory database for testing).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ecommerce.git
   cd ecommerce

2. **Create a virtual environment:**
   
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

pip install -r requirements.txt

4. **Set up the database:**

flask db upgrade

5. ** Configuration: setting Flask environment variable: **

export FLASK_ENV=development

**API Endpoints**

6. User Registration

    POST /register

    Request Body:
    {
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "password": "string"
    }

7. User Login

   POST /login
   
   Request Body:
   {
      "email": "string",
      "password": "string"
   }

8. Add Product (Admin only)

   POST /routes/products

   Request Body:
   {
      "name": "string",
      "description": "string",
      "price": "number",
      "stock": "integer"
    }

9. Place Order

   POST /routes/orders

   Request Body:

   {
      "ordFreight": "number",
      "ordTax": "number",
      "ordDate": "string (ISO 8601 format)",
      "cusId": "integer"
    }

10. Update User

    PUT /profile

    Request Body:
    {
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "password": "string"
    }




