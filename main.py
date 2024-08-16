import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn


def create_customer_table(conn):
    """ Create the customer table in the ecommerce database """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS customer (
	        cusId INTEGER PRIMARY KEY,
	        cusFirstName TEXT NOT NULL,
	        cusLastName TEXT NOT NULL,
	        cusEmail TEXT NOT NULL,
	        cusAddress TEXT NOT NULL,
	        cusCity TEXT NOT NULL,
	        cusState TEXT NOT NULL,
	        cusCountry TEXT NOT NULL,
	        cusPostalCode TEXT NOT NULL,
	        cusPhoneNumber TEXT
        );
        """
        conn.execute(sql_create_table)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")


def create_department_table(conn):
    """ Create the department table in the ecommerce database """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS department (
	        depId INTEGER PRIMARY KEY,
	        depName TEXT NOT NULL,
	        depDescription TEXT
        );
        """
        conn.execute(sql_create_table)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def create_product_table(conn):
    """ Create the product table in the ecommerce database """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS product (
	        prodId INTEGER PRIMARY KEY,
	        prodName TEXT NOT NULL,
	        prodDescription TEXT,
	        prodPrice REAL NOT NULL,
	        prodQuantity INTEGER NOT NULL,
	        depId INTEGER,
	        FOREIGN KEY (depId) REFERENCES department(depId)
        );
        """
        conn.execute(sql_create_table)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def create_order_table(conn):
    """ Create the order table in the ecommerce database """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS customerOrder (
	        ordId INTEGER PRIMARY KEY,
	        ordDate DATE NOT NULL,
   	        ordFreight REAL,
   	        ordTax REAL,
	        cusId INTEGER,
	        FOREIGN KEY(cusId) REFERENCES customer(cusId)
        );
        """
        conn.execute(sql_create_table)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def create_order_items_table(conn):
    """ Create the order items table in the ecommerce database """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS orderItems (
	        ordId INTEGER,
	        prodId INTEGER,
	        itemQuantity INTEGER NOT NULL,
	        itemPrice REAL NOT NULL,
	        PRIMARY KEY(ordId, prodId),
	        FOREIGN KEY(ordId) REFERENCES customerOrder(ordId),
	    FOREIGN KEY(prodId) REFERENCES product(prodId)
        );
        """
        conn.execute(sql_create_table)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_employee(conn, employee):
    """ Insert a new employee into the employees table """
    try:
        sql_insert_employee = """
        INSERT INTO employees (name, position, salary)
        VALUES (?, ?, ?);
        """
        conn.execute(sql_insert_employee, employee)
        conn.commit()
        print("Employee inserted successfully.")
    except Error as e:
        print(f"Error inserting employee: {e}")


def select_all_employees(conn):
    """ Query all rows in the employees table """
    try:
        sql_select_all = "SELECT * FROM employees"
        cur = conn.cursor()
        cur.execute(sql_select_all)
        rows = cur.fetchall()
        print("Employees:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error querying employees: {e}")


def main():
    database = "test_db.sqlite"

    # Create a database connection
    conn = create_connection(database)

    # Proceed if connection is successful
    if conn:
        # Create a table
        create_table(conn)

        # Insert a new employee
        employee = ('Alice', 'Developer', 70000)
        insert_employee(conn, employee)

        # Query and display all employees
        select_all_employees(conn)

        # Close the connection
        conn.close()


if __name__ == '__main__':
    main()
