"""HANDLERS MODULE
    
    This module contains the handlers for the backend. Handlers are
    functions that handle requests from the frontend.
    
    Attributes:
        bcrypt (Bcrypt): Bcrypt object for hashing passwords.
        connection (function): Function for getting a connection to the
        database.
        login_user (function): Function for logging in a user.
        register_user (function): Function for registering a user.
        get_user_by_id (function): Function for getting a user by their
"""
from backend import bcrypt
from backend.config import get_config
from .connection import connection
from .user_handlers import login_user, register_user, get_user_by_id
