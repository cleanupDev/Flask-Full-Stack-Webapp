from flask import Blueprint, jsonify
from handlers.connection import ping
from handlers.database import init_db
from handlers import login_user, register_user
from models.user import User
from flask_jwt_extended import jwt_required


config_bp = Blueprint("config", __name__)


@config_bp.route("/ping", methods=["GET"])
def ping_db():
    return ping()


@config_bp.route("/ping_auth", methods=["GET"])
@jwt_required()
def ping_auth():
    return jsonify({"status": "success", "message": "User authenticated"}), 200


@config_bp.route("/init_db", methods=["GET"])
def init_database():
    return init_db()


@config_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "success", "message": "Server is healthy"}), 200


@config_bp.route("/test_register", methods=["GET"])
def test_register():
    test_user = User(
        username="test_user",
        password="test_password",
        email="test@email",
        first_name="test_first_name",
        last_name="test_last_name",
    )
    
    return register_user(test_user)


@config_bp.route("/test_login", methods=["GET"])
def test_login():
    test_user = User(username="test_user", password="test_password")
    
    return login_user(test_user)
    