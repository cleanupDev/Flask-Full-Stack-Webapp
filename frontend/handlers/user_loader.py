import requests
import os
from cachetools import TTLCache
from models.user import User
from flask import session

BACKEND_URL = os.environ.get("BACKEND_URL", None)

ttl_cache = TTLCache(maxsize=100, ttl=300)


def load_user(user_id):
    user = ttl_cache.get(user_id)
    if user:
        return user
    else:
        user = _load_fresh_user(user_id)
        ttl_cache[user_id] = user
        return user


def _load_fresh_user(user_id):
    access_token = session.get("access_token", None)
    user_response = requests.post(BACKEND_URL + "/user", json={"data": {"id": user_id}}, headers={"Authorization": f"Bearer {access_token}"})
    if user_response.status_code == 200:
        user = User(**user_response.json["data"])
        return user
    else:
        return None


def invalidate_user_cache():
    ttl_cache.clear()