from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from backend.config import get_config

bcrypt = Bcrypt()
jwt = JWTManager()

app = Flask(__name__)

bcrypt.init_app(app)
jwt.init_app(app)
app.config.from_object(get_config())
CORS(app, origins=app.config["CORS_ORIGINS"])

from backend.blueprints import auth_bp, admin_bp

app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)