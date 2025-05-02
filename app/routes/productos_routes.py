from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.productos_models import Producto
from app.models.categoria_models import Categoria


producto_bp = Blueprint('producto', __name__, url_prefix='/productos')

# Endpoint para crear un nuevo producto
@producto_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')
    stock = data.get('stock')
    categoria_id = data.get('categoria_id')

    if not nombre or not precio or not stock or not categoria_id:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    categoria = Categoria.query.get(categoria_id)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404

    nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock, categoria_id=categoria_id)
    db.session.add(nuevo_producto)
    db.session.commit()

    return jsonify({"mensaje": "Producto creado exitosamente"}), 201

# Endpoint para listar todos los productos
@producto_bp.route('/', methods=['GET'])
def listar_productos():
    productos = Producto.query.all()
    resultado = [{"id": prod.id, "nombre": prod.nombre, "precio": prod.precio, "stock": prod.stock, "categoria": prod.categoria.nombre} for prod in productos]
    return jsonify(resultado)
