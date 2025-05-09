from flask import Flask
from app.db import db
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la base de datos usando las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Registrar los blueprints
    from app.routes.productos_routes import producto_bp
    from app.routes.categoria_routes import categoria_bp
    from app.routes.ventas_routes import ventas_bp
    from app.routes.detalle_ventas_routes import detalle_ventas_bp  # Importamos el blueprint de detalle de ventas

    app.register_blueprint(producto_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(detalle_ventas_bp)  # Registramos el blueprint de detalle de ventas

    return app
