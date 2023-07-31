from flask import Flask, render_template
from flask_login import LoginManager
from handlers import load_user
from config.config import get_config
import requests
import os

login_manager = LoginManager()

def create_app():

    app = Flask(__name__)
    app.config.from_object(get_config())
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from blueprints import auth_bp, home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])