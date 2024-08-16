from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress a warning
    db.init_app(app)

    with app.app_context():
        # Import models to ensure they're registered with SQLAlchemy
        from app.models.customer import Customer
        from app.models.department import Department
        from app.models.product import Product
        from app.models.customer_order import CustomerOrder
        from app.models.order_items import OrderItems

        # Create database tables for all models
        db.create_all()

        # Import and register Blueprints (routes)
        from app.routes.customer_routes import customer_bp
        from app.routes.department_routes import department_bp
        from app.routes.product_routes import product_bp
        from app.routes.customer_order_routes import order_bp
        from app.routes.order_items_routes import order_items_bp

        app.register_blueprint(customer_bp)
        app.register_blueprint(department_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(order_bp)
        app.register_blueprint(order_items_bp)

    @app.cli.command()
    def initdb():
        """Initialize the database."""
        db.create_all()

    @app.cli.command()
    def runserver():
        """Run the Flask development server."""
        app.run()

    return app
