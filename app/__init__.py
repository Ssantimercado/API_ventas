from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import cliente, proveedor, producto, categoria, venta


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de base de datos
    app.config.from_pyfile('../config.py')
    
    db.init_app(app)
    
    # Importar blueprints (rutas)
    from .routes.cliente import cliente_bp
    from .routes.proveedor import proveedor_bp
    from .routes.producto import producto_bp
    from .routes.categoria import categoria_bp
    from .routes.venta import venta_bp

    app.register_blueprint(cliente_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(venta_bp)

    
db.init_app(app)
    
    app.register_blueprint(producto_bp)
    app.register_blueprint(categoria_bp)

    return app
