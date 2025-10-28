from app import db

class Domicilio(db.Model):
    __tablename__ = "domicilio"
    id = db.Column(db.BigInteger, primary_key=True)
    calle = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(20), nullable=True)
    ciudad = db.Column(db.String(120), nullable=True)
    provincia = db.Column(db.String(120), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {"id": self.id, "calle": self.calle, "numero": self.numero, "ciudad": self.ciudad,
                "provincia": self.provincia, "lat": self.lat, "lon": self.lon}
