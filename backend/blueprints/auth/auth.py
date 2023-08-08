from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User
from backend.handlers import login_user, register_user, get_user_by_id
import logging

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    user = User(**request.json["data"])
    logging.debug("Logging in user: " + user.username)

    return login_user(user)


@auth_bp.route("/register", methods=["POST"])
def register():
    user = User(**request.json["data"])
    logging.debug("Registering user: " + user.username)

    return register_user(user)


@auth_bp.route("/user", methods=["GET"])
@jwt_required()
def user():
    current_user_id = get_jwt_identity()
    logging.debug("Getting user: " + str(current_user_id))

    return get_user_by_id(current_user_id)
