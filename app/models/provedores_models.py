from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    pagina_web = db.Column(db.String(100))
