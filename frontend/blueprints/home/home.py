from flask import Blueprint, jsonify, request, render_template

home_bp = Blueprint("home_bp", __name__, template_folder="templates")


@home_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@home_bp.route("/home", methods=["GET"])
def home():
    return render_template("home.html")