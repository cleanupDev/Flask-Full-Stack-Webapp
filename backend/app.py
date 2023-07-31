from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from config.config import get_config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from blueprints.config.config import config_bp

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config = get_config()
jwt = JWTManager(app)


app.register_blueprint(config_bp)



if __name__ == '__main__':
    app.run(debug=app.config.DEBUG)
