
from flask import Blueprint, request, jsonify
from models.clientes_models import Cliente, Telefono, db

clientes_bp = Blueprint('clientes_bp', __name__)

@clientes_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    campos = ['rut', 'nombre', 'calle', 'numero', 'comuna', 'ciudad', 'telefonos']
    if not all(k in data for k in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    if not isinstance(data['telefonos'], list) or not data['telefonos']:
        return jsonify({'error': 'Debe proporcionar al menos un teléfono'}), 400

    nuevo_cliente = Cliente(
        rut=data['rut'],
        nombre=data['nombre'],
        calle=data['calle'],
        numero=data['numero'],
        comuna=data['comuna'],
        ciudad=data['ciudad']
    )
    for tel in data['telefonos']:
        nuevo_cliente.telefonos.append(Telefono(numero=tel))

    db.session.add(nuevo_cliente)
    db.session.commit()

    return jsonify({'mensaje': 'Cliente creado correctamente'}), 201

@clientes_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    resultado = []
    for cliente in clientes:
        resultado.append({
            'id': cliente.id,
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'direccion': {
                'calle': cliente.calle,
                'numero': cliente.numero,
                'comuna': cliente.comuna,
                'ciudad': cliente.ciudad
            },
            'telefonos': [t.numero for t in cliente.telefonos]
        })
    return jsonify(resultado), 200
