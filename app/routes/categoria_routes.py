from flask import Blueprint, request, jsonify
from app.db import db
from app.models.categoria_models import Categoria  # Modelo Categoria
from app.models.productos_models import Producto  # Modelo Producto

categoria_bp = Blueprint('categoria', __name__, url_prefix='/categorias')

# Endpoint para crear una nueva categoría
@categoria_bp.route('/', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')

    if not nombre or not descripcion:
        return jsonify({"error": "Nombre y descripción son obligatorios"}), 400

    nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
    db.session.add(nueva_categoria)
    db.session.commit()

    return jsonify({"mensaje": "Categoría creada exitosamente"}), 201

# Endpoint para listar categorias
@categoria_bp.route('/', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()
    resultado = [categoria.serialize() for categoria in categorias]
    return jsonify(resultado)


# Endpoint para obtener una categoría específica
@categoria_bp.route('/<int:id>', methods=['GET'])
def obtener_categoria(id):
    categoria = Categoria.query.get(id)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404

    return jsonify({
        "id": categoria.id,
        "nombre": categoria.nombre,
        "descripcion": categoria.descripcion
    })

