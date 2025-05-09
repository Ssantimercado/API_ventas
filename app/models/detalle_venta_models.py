from app.db import db

class DetalleVenta(db.Model):
    __tablename__ = 'detalles_venta'

    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    producto_id = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    def __init__(self, venta_id, producto_id, precio_unitario, cantidad, subtotal):
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.subtotal = subtotal

    def serialize(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'producto_id': self.producto_id,
            'precio_unitario': self.precio_unitario,
            'cantidad': self.cantidad,
            'subtotal': self.subtotal
        }

    def __repr__(self):
        return f"<DetalleVenta venta_id={self.venta_id} producto_id={self.producto_id}>"
