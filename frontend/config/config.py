import os
from dotenv import dotenv_values


class Config:
    DEBUG = False
    SECRET_KEY = "default_secret_key"
    HOST = "localhost"
    PORT = 5000
    BACKEND_URL = "http://localhost:5001"
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    HOST = dotenv_values("frontend/config/frontend.env").get("HOST")
    PORT = dotenv_values("frontend/config/frontend.env").get("PORT")
    BACKEND_URL = dotenv_values("frontend/config/frontend.env").get("BACKEND_URL")
    
    
class ProductionConfig(Config):
    DEBUG = False
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    BACKEND_URL = os.environ.get("BACKEND_URL")
    
    
def get_config(environment=os.environ.get("ENVIRONMENT", "development")):
    if environment == "production":
        return ProductionConfig()
    else:
        return DevelopmentConfig()