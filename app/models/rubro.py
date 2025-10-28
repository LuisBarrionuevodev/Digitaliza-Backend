from app import db

class Rubro(db.Model):
    __tablename__ = "rubro"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)
    activo = db.Column(db.Boolean, nullable=False, server_default=db.text("1"))

    def to_dict(self): return {"id": self.id, "nombre": self.nombre, "activo": self.activo}
