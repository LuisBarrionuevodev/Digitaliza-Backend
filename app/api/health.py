from flask import Blueprint
bp = Blueprint("health", __name__)

@bp.get("")
def health():
    return {"status": "ok"}, 200
