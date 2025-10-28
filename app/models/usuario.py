from app import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "email": self.email}
