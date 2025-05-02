from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Inicializar la extensión de la base de datos
db = SQLAlchemy()

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la base de datos usando las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Registrar las rutas dentro de la función create_app
    from app.routes.productos_routes import producto_bp
    from app.routes.categoria_routes import categoria_bp
    
    app.register_blueprint(producto_bp)
    app.register_blueprint(categoria_bp)

    return app
