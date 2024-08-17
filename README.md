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
       "email": "john.doe@example.com",
       "first_name": "John",
       "last_name": "Doe",
       "password": "newpassword456",
       "address": "456 Maple Avenue",
       "city": "Shelbyville",
       "state": "IL",
       "country": "USA",
       "postal_code": "62565",
       "phone_number": "+1-555-987-6543"
   }

7. User Login

   POST /login
   
   Request Body:
   {
     "email": "john.doe@example.com",
     "password": "userpassword"
   }

8. Add Product (Admin only)

   POST /routes/products

   Request Body:
   {
     "prodName": "Acer Computer i7",
     "prodDescription": "SSD 524GB e 16GB RAM",
     "prodPrice": 5999.99,
     "prodQuantity": 10,
     "depId": 1
   }


9. Place Order

   POST /routes/orders

   Request Body:

   {
       "order_date": "2024-08-17",
       "order_freight": 0.5,
       "order_tax": 3.7,
       "items": [
        {
            "product_id": 3,
            "quantity": 5
        },
        {
            "product_id": 4,
            "quantity": 6
        }
       ]
   }


10. Update User

    PUT /profile

    Request Body:
    {
       "email": "john.doe@example.com",
       "password": "userpassword"  // replace with the actual password
   }


11. Running the Application

   flask run

12. Running Tests

   pytest

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    Flask
    SQLAlchemy
    Flask-JWT-Extended
    Werkzeug



