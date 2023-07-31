from flask import Blueprint, request
from models.user import User
from handlers import login_user, register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    user = User(**request.json["data"])

    return login_user(user)


@auth_bp.route("/register", methods=["POST"])
def register():
    user = User(**request.json["data"])

    return register_user(user)
