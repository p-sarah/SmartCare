from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from models import db
from config import Config
from routes.auth_routes import auth_bp

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth_bp)
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    @app.route("/")
    def home():
        return {
            "project": "SmartCare",
            "version": "1.0",
            "status": "Running Successfully"
        }
    return app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)