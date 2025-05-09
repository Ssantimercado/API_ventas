from flask import Blueprint, request, jsonify
from app.db import db
from app.models.detalle_venta_models import DetalleVenta

detalle_ventas_bp = Blueprint('detalle_ventas', __name__, url_prefix='/detalles_ventas')

# Endpoint para registrar un detalle de venta
@detalle_ventas_bp.route('/', methods=['POST'])
def registrar_detalle_venta():
    data = request.get_json()

    venta_id = data.get('venta_id')
    producto_id = data.get('producto_id')
    cantidad = data.get('cantidad')
    precio_unitario = data.get('precio_unitario')

    if not venta_id or not producto_id or not cantidad or not precio_unitario:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    # Calcular el subtotal
    subtotal = cantidad * precio_unitario

    # Crear el nuevo detalle de venta
    detalle_venta = DetalleVenta(
        venta_id=venta_id,
        producto_id=producto_id,
        cantidad=cantidad,
        precio_unitario=precio_unitario,
        subtotal=subtotal
    )

    db.session.add(detalle_venta)
    db.session.commit()

    return jsonify({"mensaje": "Detalle de venta registrado exitosamente", "detalle_venta": detalle_venta.serialize()}), 201
