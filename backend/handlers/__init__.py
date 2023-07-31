from app import bcrypt
from config.config import get_config
from .connection import connection
from .user_handlers import login_user, register_user, get_user_by_id