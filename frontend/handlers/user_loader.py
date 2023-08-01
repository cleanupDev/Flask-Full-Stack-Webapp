import requests
import os
from cachetools import TTLCache
from models.user import User
from flask import session
from dotenv import dotenv_values
import logging

BACKEND_URL = dotenv_values("frontend/config/frontend.env").get("BACKEND_URL")

ttl_cache = TTLCache(maxsize=100, ttl=300)


def load_user(user_id):
    user = ttl_cache.get(user_id)
    if user:
        logging.debug("User found in cache")
        return user
    else:
        logging.debug("Loading fresh user")
        user = _load_fresh_user(user_id)
        ttl_cache[user_id] = user
        return user


def _load_fresh_user(user_id):
    access_token = session.get("access_token", None)
    user = User(id=user_id)
    user_response = requests.get(BACKEND_URL + "/user", headers={"Authorization": f"Bearer {access_token}"})
    if user_response.status_code == 200:
        user = User(**user_response.json()["data"])
        return user
    else:
        return None


def invalidate_user_cache():
    ttl_cache.clear()