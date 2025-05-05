from app.db import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(100), nullable=False)

   


    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }

    def __repr__(self):
        return f"<Categoria {self.nombre}>"
