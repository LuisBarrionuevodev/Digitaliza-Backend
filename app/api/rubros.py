from flask import Blueprint, request
from app import db
from app.models import Rubro

bp = Blueprint("rubros", __name__)

@bp.get("")
def listar():
    items = Rubro.query.order_by(Rubro.id.desc()).all()
    return {"items": [r.to_dict() for r in items]}, 200

@bp.post("")
def crear():
    data = request.get_json(force=True) or {}
    nombre = (data.get("nombre") or "").strip()
    if not nombre: return {"error":"nombre es obligatorio"}, 400
    if Rubro.query.filter_by(nombre=nombre).first(): return {"error":"rubro ya existe"}, 409
    r = Rubro(nombre=nombre)
    db.session.add(r); db.session.commit()
    return r.to_dict(), 201
