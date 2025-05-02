from flask import Blueprint, request, jsonify
from app import db
from app.models.categoria_models import Categoria  



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

# Endpoint para listar todas las categorías
@categoria_bp.route('/', methods=['GET'])
def listar_categorias():
    categorias = Categoria.query.all()
    resultado = [{"id": cat.id, "nombre": cat.nombre, "descripcion": cat.descripcion} for cat in categorias]
    return jsonify(resultado)
