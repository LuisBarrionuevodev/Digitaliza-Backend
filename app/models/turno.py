from app import db

class Turno(db.Model):
    __tablename__ = "turno"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)

    def to_dict(self): return {"id": self.id, "nombre": self.nombre}
