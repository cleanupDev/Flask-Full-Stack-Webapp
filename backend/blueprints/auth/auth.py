from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.user import User
from handlers import login_user, register_user, get_user_by_id

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    user = User(**request.json["data"])

    return login_user(user)


@auth_bp.route("/register", methods=["POST"])
def register():
    user = User(**request.json["data"])

    return register_user(user)


@auth_bp.route("/user", methods=["POST"])
@jwt_required()
def user():
    user = User(**request.json["data"])
    
    return get_user_by_id(user)

