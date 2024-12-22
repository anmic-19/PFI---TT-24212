# FUNCIONES DE LA BASE DE DATOS

import sqlite3
from colorama import init, Fore, Back, Style
init(autoreset=True)

# CONSTANTES
ruta_db = r"C:\Users\USUARIO\Downloads\Curso Python - Talento Tech - 2024\ENTREGA PFI\inventario.db"


# FUNCIONES
"""
db_crear_tabla_productos()

Esta función utiliza a sqlite3 para conectarse con la base "inventario.db" y crea 
la tabla productos
"""
def db_crear_tabla_productos():
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )"""
        )
        conexion.commit()
        print("El registro se insertó exitosamente")
        conexion.close()


"""
db_insertar_producto(producto)

1. recibe como argumento un diccionario con las clave/valor de cada campo de la tabla
2. inserta los datos en la tabla productos
"""
def db_insertar_producto(producto):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?,?,?,?,?)"
    placeholders = (
        producto["nombre"],
        producto["descripcion"],
        producto["categoria"],
        producto["cantidad"],
        producto["precio"],
    )
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


"""
db_get_productos()

1. lee todos los datos de la tabla productos
2. retorna una lista de tuplas con los datos de la tabla
"""
def db_get_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()  
    conexion.close()
    return lista_productos


"""
db_get_producto_by_id(id)

1. busco y retorno el registro según el id
2. retorno una tupla con el resultado
"""
def db_get_producto_by_id(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", id)
    producto = cursor.fetchone()
    conexion.close()
    return producto


"""
db_actualizar_producto(id, nueva_cantidad)

1. actualiza la cantidad del producto según el id
"""
def db_actualizar_producto(id, nueva_cant):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", id, nueva_cant)
    conexion.commit()
    conexion.close()


"""
db_eliminar_producto(id)

1. eliminar de la tabla el producto con el id que recibo como argumento
"""
def db_eliminar_producto(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", id)
    conexion.commit()
    conexion.close()


"""
db_get_productos_by_condicion(minimo_stock)

1. retornar una lista_producto con aquellos registros cuya cantidad < minimo_stock
"""
def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad < ?", minimo_stock)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos
