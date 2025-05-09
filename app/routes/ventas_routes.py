from flask import Blueprint, request, jsonify
from datetime import datetime
from app.db import db
from app.models.venta_models import Venta
from app.models.detalle_venta_models import DetalleVenta

ventas_bp = Blueprint('ventas', __name__, url_prefix='/ventas')

# Endpoint para registrar una nueva venta
@ventas_bp.route('/', methods=['POST'])
def registrar_venta():
    data = request.get_json()

    cliente_id = data.get('cliente_id')
    descuento = data.get('descuento', 0)
    productos = data.get('productos')  # Lista de productos con: producto_id, cantidad, precio_unitario

    if not cliente_id or not productos:
        return jsonify({"error": "cliente_id y productos son obligatorios"}), 400

    total = 0
    detalles = []

    for item in productos:
        producto_id = item.get('producto_id')
        cantidad = item.get('cantidad')
        precio_unitario = item.get('precio_unitario')

        if not producto_id or not cantidad or not precio_unitario:
            return jsonify({"error": "Cada producto debe tener producto_id, cantidad y precio_unitario"}), 400

        subtotal = cantidad * precio_unitario
        total += subtotal

        detalle = DetalleVenta(
            venta_id=None,  # Se asignará después de crear la venta
            producto_id=producto_id,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            subtotal=subtotal
        )
        detalles.append(detalle)

    venta = Venta(
        fecha=datetime.utcnow(),
        cliente_id=cliente_id,
        descuento=descuento,
        total=total - descuento
    )
    db.session.add(venta)
    db.session.commit()  # Ahora venta tiene un ID

    for detalle in detalles:
        detalle.venta_id = venta.id
        db.session.add(detalle)

    db.session.commit()

    return jsonify({"mensaje": "Venta registrada", "venta_id": venta.id}), 201
