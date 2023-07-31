from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required

home_bp = Blueprint("home_bp", __name__, template_folder="templates")


@home_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@home_bp.route("/home", methods=["GET"])
@login_required
def home():
    return render_template("home.html")