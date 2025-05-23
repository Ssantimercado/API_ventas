from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    comuna = db.Column(db.String(50), nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)
    telefonos = db.relationship('Telefono', backref='cliente', lazy=True, cascade="all, delete-orphan")

class Telefono(db.Model):
    __tablename__ = 'telefonos'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)