import os
from dotenv import dotenv_values
import logging


class Config:
    DEBUG = False
    SECRET_KEY = "default_secret_key"
    HOST = "localhost"
    PORT = 5000
    BACKEND_URL = "http://localhost:5001"


class DevelopmentConfig(Config):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Frontend running in development mode")

    _frontend_env = dotenv_values("frontend/config/frontend.env")

    DEBUG = True

    # Either use .env file or environment variables in docker container
    HOST = _frontend_env.get("HOST") or os.environ.get("HOST")

    PORT = _frontend_env.get("PORT") or os.environ.get("PORT")

    BACKEND_URL = _frontend_env.get("BACKEND_URL") or os.environ.get("BACKEND_URL")


class ProductionConfig(Config):
    logging.basicConfig(level=logging.INFO)
    logging.info("Frontend running in production mode")
    DEBUG = False
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    BACKEND_URL = os.environ.get("BACKEND_URL")


def get_config(environment=os.environ.get("ENVIRONMENT", "development")):
    if environment == "production":
        return ProductionConfig()
    else:
        return DevelopmentConfig()
