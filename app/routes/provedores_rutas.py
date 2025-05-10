from flask import Blueprint, request, jsonify
from provedores_models import db, Proveedor

bp_proveedores = Blueprint('bp_proveedores', __name__)

# Crear un nuevo proveedor
@bp_proveedores.route('/proveedores', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    
    rut = data.get('rut')
    nombre = data.get('nombre')
    direccion = data.get('direccion')
    telefono = data.get('telefono')
    pagina_web = data.get('pagina_web', '')

    if not all([rut, nombre, direccion, telefono]):
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    nuevo = Proveedor(
        rut=rut,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        pagina_web=pagina_web
    )
    db.session.add(nuevo)
    db.session.commit()

    return jsonify({'mensaje': 'Proveedor creado correctamente', 'id': nuevo.id}), 201

# Listar todos los proveedores
@bp_proveedores.route('/proveedores', methods=['GET'])
def listar_proveedores():
    proveedores = Proveedor.query.all()
    resultado = []

    for p in proveedores:
        resultado.append({
            'id': p.id,
            'rut': p.rut,
            'nombre': p.nombre,
            'direccion': p.direccion,
            'telefono': p.telefono,
            'pagina_web': p.pagina_web
        })

    return jsonify(resultado)
