from flask import Flask
from flask_login import LoginManager
from frontend.handlers import load_user
from frontend.config import get_config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    config = get_config()
    config.setup_logging()
    app.config.from_object(config)
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from frontend.blueprints import auth_bp, home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
