from flask import Blueprint, request, jsonify

index_bp = Blueprint("index", __name__)


@index_bp.route("/", methods=["GET"])
def index():
    return jsonify({"status": "success", "message": "Backend running"}), 200


@index_bp.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "message": "Route not found"}), 404
