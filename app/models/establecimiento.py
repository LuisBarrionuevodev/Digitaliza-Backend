from app import db

class Establecimiento(db.Model):
    __tablename__ = "establecimiento"
    id = db.Column(db.BigInteger, primary_key=True)
    contribuyente_id = db.Column(db.BigInteger, db.ForeignKey("contribuyente.id"), nullable=False)
    nombre_fantasia = db.Column(db.String(255), nullable=True)

    contribuyente = db.relationship("Contribuyente", backref="establecimientos")

    def to_dict(self):
        return {"id": self.id, "contribuyente_id": self.contribuyente_id, "nombre_fantasia": self.nombre_fantasia}
