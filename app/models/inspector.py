from app import db

class Inspector(db.Model):
    __tablename__ = "inspector"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    turno_id = db.Column(db.Integer, db.ForeignKey("turno.id"), nullable=False)

    turno = db.relationship("Turno")

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre,
                "turno_id": self.turno_id, "turno": self.turno.to_dict() if self.turno else None}
