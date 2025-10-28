from datetime import date
from app import db

class EstablecimientoDomicilio(db.Model):
    __tablename__ = "establecimiento_domicilio"
    id = db.Column(db.BigInteger, primary_key=True)
    establecimiento_id = db.Column(db.BigInteger, db.ForeignKey("establecimiento.id"), nullable=False)
    domicilio_id = db.Column(db.BigInteger, db.ForeignKey("domicilio.id"), nullable=False)
    fecha_desde = db.Column(db.Date, nullable=False)
    fecha_hasta = db.Column(db.Date, nullable=True)

    establecimiento = db.relationship("Establecimiento")
    domicilio = db.relationship("Domicilio")

    def activo(self) -> bool:
        return self.fecha_hasta is None

    def to_dict(self):
        return {"id": self.id, "establecimiento_id": self.establecimiento_id, "domicilio_id": self.domicilio_id,
                "fecha_desde": self.fecha_desde.isoformat(),
                "fecha_hasta": self.fecha_hasta.isoformat() if self.fecha_hasta else None}
