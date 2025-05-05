from app.db import db
from app.models.categoria_models import Categoria
  

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float(30), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    categoria = db.relationship('Categoria', backref=db.backref('productos', lazy=True))

    def __init__(self, nombre, precio, stock, categoria_id):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'categoria_id': self.categoria_id,
            'categoria': {
                'id': self.categoria.id,
                'nombre': self.categoria.nombre,
                'descripcion': self.categoria.descripcion
            } if self.categoria else None
        }

    def __repr__(self):
        return f"<Producto {self.nombre}>"
