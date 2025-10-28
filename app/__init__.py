import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import get_config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name: str | None = None):
    app = Flask(__name__)
    cfg = get_config(config_name)
    app.config.from_object(cfg)

    db.init_app(app)
    migrate.init_app(app, db)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    @app.get("/")
    def root():
        return {"message": "Bromato API lista"}, 200

    return app
