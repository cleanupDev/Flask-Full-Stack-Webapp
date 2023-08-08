from flask import Blueprint, jsonify, request, render_template, session
from flask_login import login_user, login_required, logout_user
from frontend.handlers import remove_user_from_cache
from models import User
import requests
from dotenv import dotenv_values

BACKEND_URL = dotenv_values("frontend/config/frontend.env").get("BACKEND_URL")

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = User(**request.form.to_dict())
        login_response = requests.post(
            BACKEND_URL + "/login", json={"data": user.to_dict()}
        )

        if login_response.status_code == 200:
            login_user(User(**login_response.json()["data"]))
            session["access_token"] = login_response.json()["access_token"]
            response = {
                "status": login_response.json()["status"],
                "message": login_response.json()["message"],
                "redirect_url": "/home",
            }
            return jsonify(response), 200

        else:
            response = {
                "status": login_response.json()["status"],
                "message": login_response.json()["message"],
                "redirect_url": "/login",
            }
            return jsonify(response), 401

    else:
        return jsonify({"status": "error", "message": "Method not allowed"}), 405


@auth_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    remove_user_from_cache()
    logout_user()
    session.pop("access_token", None)
    return (
        jsonify({"status": "success", "message": "User logged out successfully"}),
        200,
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user = User(**request.form.to_dict())
        register_response = requests.post(
            BACKEND_URL + "/register", json={"data": user.to_dict()}
        )

        if register_response.status_code == 201:
            response = {
                "status": register_response.json()["status"],
                "message": register_response.json()["message"],
                "redirect_url": "/login",
            }
            return jsonify(response), 201

        else:
            response = {
                "status": register_response.json()["status"],
                "message": register_response.json()["message"],
                "redirect_url": "/register",
            }
            return jsonify(response), 400

    else:
        return jsonify({"status": "error", "message": "Method not allowed"}), 405
