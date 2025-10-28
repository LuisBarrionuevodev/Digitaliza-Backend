from app import db

class Contribuyente(db.Model):
    __tablename__ = "contribuyente"
    id = db.Column(db.BigInteger, primary_key=True)
    tipo_doc = db.Column(db.String(10), nullable=False)   # DNI, CUIT, etc.
    nro_doc  = db.Column(db.String(20), nullable=False)
    nombre   = db.Column(db.String(255), nullable=False)

    __table_args__ = (db.UniqueConstraint("tipo_doc", "nro_doc", name="uq_contribuyente_doc"),)

    def to_dict(self):
        return {"id": self.id, "tipo_doc": self.tipo_doc, "nro_doc": self.nro_doc, "nombre": self.nombre}
