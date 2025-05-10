# API_ventas
API RESTful para gestionar un sistema de ventas, permitiendo registrar y consultar proveedores, clientes, productos, categorías y ventas. Incluye control de stock, registro de precios históricos, aplicación de descuentos y cálculo automático del total en cada venta, optimizando la gestión comercial de la empresa.





KoScKa:

Archivos Agregados
models/clientes_models.py: define los modelos Cliente y Telefono con relación uno a muchos.

routes/clientes_routes.py: contiene los endpoints:

POST /clientes: para registrar un cliente con múltiples teléfonos.

GET /clientes: para listar todos los clientes registrados.