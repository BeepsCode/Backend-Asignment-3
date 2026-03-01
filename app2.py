from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria con tu estructura
productos_db = []

@app.route('/crear_producto', methods=['POST'])
def crear_producto():
    datos = request.get_json()
    
    # Actualizamos la lista de campos requeridos para que coincida con tu JSON
    campos_requeridos = ['nombre', 'descripcion', 'precio', 'moneda', 'stock', 'categoria']
    
    # Verificamos si falta algún campo del nuevo diseño
    if not datos or not all(k in datos for k in campos_requeridos):
        return jsonify({
            "error": "Datos de producto incompletos",
            "campos_esperados": campos_requeridos
        }), 400

    # Si todo está bien, creamos el producto con todos los campos
    nuevo_prod = {
        "id": 100 + len(productos_db) + 1,
        "nombre": datos['nombre'],
        "descripcion": datos['descripcion'],
        "precio": datos['precio'],
        "moneda": datos['moneda'],
        "stock": datos['stock'],
        "categoria": datos['categoria']
    }
    
    productos_db.append(nuevo_prod)
    return jsonify({"mensaje": "Producto creado", "producto": nuevo_prod}), 201

@app.route('/productos', methods=['GET'])
def listar_productos():
    # Retorna la lista completa de productos y el conteo actual
    return jsonify({
        "total": len(productos_db),
        "productos": productos_db
    }), 200

# --- BASES DE DATOS EN MEMORIA ---
usuarios_db = []
productos_db = []
empleados_db = []  # <--- Nueva lista para empleados

# --- RUTAS DE EMPLEADOS ---

@app.route('/empleados', methods=['GET'])
def listar_empleados():
    return jsonify({
        "total": len(empleados_db),
        "empleados": empleados_db
    })

@app.route('/crear_empleado', methods=['POST'])
def crear_empleado():
    datos = request.get_json()
    
    # Definimos qué datos necesita un empleado
    campos_empleado = ['nombre', 'puesto', 'salario']
    
    if not datos or not all(k in datos for k in campos_empleado):
        return jsonify({
            "error": "Datos de empleado incompletos",
            "requerido": campos_empleado
        }), 400

    nuevo_empleado = {
        "id": 500 + len(empleados_db) + 1, # IDs empiezan en 501
        "nombre": datos['nombre'],
        "puesto": datos['puesto'],
        "salario": datos['salario'],
        "activo": True
    }
    
    empleados_db.append(nuevo_empleado)
    return jsonify({"mensaje": "Empleado registrado", "empleado": nuevo_empleado}), 201

if __name__ == '__main__':
    app.run(debug=True)