from flask import Blueprint, request, jsonify
from models.user import User
from handlers.user_handlers import login_user, register_user

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/login', methods=['POST'])
def login():
    user = User(**request.json['data'])
    
    return login_user(user)


@auth_bp.route('/register', methods=['POST'])
def register():
    user = User(**request.json['data'])
    
    return register_user(user)