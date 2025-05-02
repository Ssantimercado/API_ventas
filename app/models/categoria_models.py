from app.extensions import db



class Categoria(db.Model):
    __tablename__ = 'Categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(255), nullable=False)

    productos = db.relationship('Producto', backref='categoria', lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nombre}>"
