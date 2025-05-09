from app.db import db

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, nullable=False)
    descuento = db.Column(db.Float, default=0)
    total = db.Column(db.Float, nullable=False)

    detalles = db.relationship('DetalleVenta', backref='venta', lazy=True)

    def __init__(self, fecha, cliente_id, descuento, total):
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.descuento = descuento
        self.total = total

    def serialize(self):
        return {
            'id': self.id,
            'fecha': self.fecha.isoformat(),
            'cliente_id': self.cliente_id,
            'descuento': self.descuento,
            'total': self.total,
            'detalles': [d.serialize() for d in self.detalles]
        }

    def __repr__(self):
        return f"<Venta {self.id}>"
