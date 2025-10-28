from flask import Blueprint

api_bp = Blueprint("api", __name__)

from .health import bp as health_bp
from .rubros import bp as rubros_bp


api_bp.register_blueprint(health_bp, url_prefix="/health")
api_bp.register_blueprint(rubros_bp, url_prefix="/rubros")
