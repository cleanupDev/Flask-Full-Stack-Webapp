"""Blueprints module for the backend.

This module contains the blueprints for the backend.

Attributes:
    auth_bp (Blueprint): Blueprint for the auth routes.
    admin_bp (Blueprint): Blueprint for the admin routes.
"""

from .index.index import index_bp
from .auth.auth import auth_bp
from .admin.admin import admin_bp
