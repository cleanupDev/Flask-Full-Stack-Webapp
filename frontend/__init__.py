from flask import Flask
from flask_login import LoginManager
from handlers import load_user
from config.config import get_config

login_manager = LoginManager()

app = Flask(__name__)

app.config.from_object(get_config())
login_manager.init_app(app)
login_manager.user_loader(load_user)

from blueprints import auth_bp, home_bp

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
