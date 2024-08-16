from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


# Initialize SQLAlchemy, Migrate, and JWTManager
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress a warning
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Set this to a secure random value

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

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
        from app.auth_routes import auth_bp
        from app.routes.setup_bp import setup_bp

        app.register_blueprint(customer_bp)
        app.register_blueprint(department_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(order_bp)
        app.register_blueprint(order_items_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(setup_bp)

    @app.cli.command()
    def initdb():
        """Initialize the database."""
        db.create_all()

    @app.cli.command()
    def runserver():
        """Run the Flask development server."""
        app.run()

    return app
