from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="2002",
        db="biblioteca",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/libros', methods=['GET'])
def obtener_libros():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()
    conexion.close()
    return jsonify(libros)

@app.route('/libros', methods=['POST'])
def crear_libro():
    nuevo_libro = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO libros (titulo, autor) VALUES (%s, %s)"
        cursor.execute(sql, (nuevo_libro['titulo'], nuevo_libro['autor']))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Libro creado'}), 201

@app.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro_actualizado = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "UPDATE libros SET titulo=%s, autor=%s WHERE id=%s"
        cursor.execute(sql, (libro_actualizado['titulo'], libro_actualizado['autor'], id))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Libro actualizado'})

@app.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "DELETE FROM libros WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Libro eliminado'})


@app.route('/prestamos', methods=['GET'])
def obtener_prestamos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM prestamos")
        prestamos = cursor.fetchall()
    conexion.close()
    return jsonify(prestamos)

@app.route('/prestamos', methods=['POST'])
def crear_prestamo():
    nuevo_prestamo = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "INSERT INTO prestamos (libro_id, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nuevo_prestamo['libro_id'], nuevo_prestamo['fecha_prestamo'], nuevo_prestamo['fecha_devolucion']))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Préstamo creado'}), 201

@app.route('/prestamos/<int:id>', methods=['PUT'])
def actualizar_prestamo(id):
    prestamo_actualizado = request.get_json()
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "UPDATE prestamos SET libro_id=%s, fecha_prestamo=%s, fecha_devolucion=%s WHERE id=%s"
        cursor.execute(sql, (prestamo_actualizado['libro_id'], prestamo_actualizado['fecha_prestamo'], prestamo_actualizado['fecha_devolucion'], id))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Préstamo actualizado'})

@app.route('/prestamos/<int:id>', methods=['DELETE'])
def eliminar_prestamo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = "DELETE FROM prestamos WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
    conexion.close()
    return jsonify({'mensaje': 'Préstamo eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
