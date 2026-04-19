import os
from flask import Flask

from app.config import Config
from app.routes.auth_routes import auth_bp
from app.routes.llm_routes import llm_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["SQLITE_BASE_PATH"], exist_ok=True)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(llm_bp)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}, 200

    return app
