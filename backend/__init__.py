"""BACKEND MODULE
    
    This module is the backend of the application. It contains the main
    application and the blueprints for the backend.
    
    Attributes:
        bcrypt (Bcrypt): Bcrypt object for hashing passwords.
        jwt (JWTManager): JWTManager object for managing JWTs.
        app (Flask): Flask application object.
"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from backend.config import get_config

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    bcrypt.init_app(app)
    jwt.init_app(app)
    config = get_config()
    config.setup_logging()
    app.config.from_object(config)
    CORS(app, origins=app.config["CORS_ORIGINS"])

    from backend.blueprints import index_bp, auth_bp, admin_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
