from flask import Flask
from flask_bcrypt import Bcrypt
from config.config import get_config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.config.from_object(get_config())
    CORS(app, origins=app.config["CORS_ORIGINS"])

    from blueprints import auth_bp, config_bp

    app.register_blueprint(config_bp)
    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
