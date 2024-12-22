# FUNCIONES DEL MENU

from fx_db import *
from colorama import init, Fore, Back, Style
init(autoreset=True)

"""
Mostrar opciones: La aplicación debe mostrar en la consola las opciones disponibles y 
retornar la opción seleccionada
"""
def menu_mostrar_opciones() :
    print("-" * 30)
    print(Style.BRIGHT + Fore.BLUE + Back.WHITE + "Menú principal")
    print("-" * 30)
    print(Style.BRIGHT + Fore.CYAN + 
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input(Fore.YELLOW + "Seleccione una opción del 1 al 7: ")
    return opcion


"""
Registro de productos: La aplicación debe permitir al usuario agregar nuevos productos 
al inventario, solicitando los siguientes datos: nombre, descripción, cantidad, precio y
categoría.
"""
def menu_registrar_producto():
    print(Style.BRIGHT + "\nPara registrar un producto, ingrese los siguientes datos:")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    # Diccionario 
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insertar_producto(producto)
    print(Style.BRIGHT + Fore.GREEN + "\nProducto insertado exitosamente")


"""
Visualización de productos: La aplicación debe mostrar todos los productos registrados 
en el inventario, incluyendo su ID, nombre, descripción, cantidad, precio y categoría.
"""
def menu_mostrar_productos():
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print(Style.BRIGHT + "No hay productos para mostrar")


"""
Actualización de productos: La aplicación debe permitir al usuario actualizar la cantidad 
disponible de un producto específico utilizando su ID.
"""
def menu_actualizar_producto():
    id = int(input("Ingrese el id del producto que quiere actualizar: "))
    producto = db_get_producto_by_id(id)
    if producto:
        print(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        db_actualizar_producto(nueva_cantidad, id)
        print(Fore.GREEN + "Cantidad actualizada!")
    else:
        print(Fore.RED + "No existe el producto con el id ingresado")


"""
Eliminación de productos: La aplicación debe permitir al usuario eliminar un producto 
del inventario utilizando su ID.
"""
def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto que quiere eliminar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print(Fore.RED + "ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(Fore.RED + Back.YELLOW + "\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print(Fore.GREEN + "Registro eliminado!")
        else:
            print(Fore.RED + "Operación cancelada.")


"""
Búsqueda de productos: La aplicación debe ofrecer una funcionalidad para buscar productos 
por su ID, mostrando los resultados que coincidan con los criterios de búsqueda. De
manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
"""
def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print(Fore.RED + "ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)


"""
Reporte de Bajo Stock: La aplicación debe generar un reporte de productos que tengan 
una cantidad igual o inferior a un límite especificado por el usuario.
"""
def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock: "))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)