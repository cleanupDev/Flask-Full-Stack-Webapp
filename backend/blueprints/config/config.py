from flask import Blueprint, request, jsonify
from handlers.connection import ping
from handlers.database import init_db
from flask_jwt_extended import jwt_required


config_bp = Blueprint("config", __name__)


@config_bp.route("/ping_db", methods=["GET"])
def ping_db():
    return ping()


@config_bp.route("/ping_auth", methods=["GET"])
@jwt_required()
def ping_auth():
    return jsonify({"status": "success", "message": "User authenticated"}), 200


@config_bp.route("/init_db", methods=["GET"])
def init_database():
    return init_db()
