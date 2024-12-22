# PROYECTO FINAL INTEGRADOR 
# Entrega de proyecto final curso C24212 Talento Tech
# ALUMNA: María de los Ángeles Miceli Baro


# SE IMPORTAN LAS FUNCIONES
from fx_menu import *
from fx_db import db_crear_tabla_productos
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Funcion principal main
def main():
    # Se inicializa la base de datos y se crea la tabla si no existe
    db_crear_tabla_productos()

    # Cuerpo de la función main
    while True:
        opcion = menu_mostrar_opciones()
        print("Ha seleccionado la opción: ", opcion)

        if opcion == "1":
            menu_registrar_producto()
        elif opcion == "2":
            menu_mostrar_productos()
        elif opcion == "3":
            menu_actualizar_producto()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            menu_reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.BLUE + Back.WHITE + "Gracias por usar nuestra App! Vuelva pronto")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, elija una opción válida.")

        salir = input(Fore.YELLOW + "\nIngrese 's' para salir o cualquier tecla para continuar: ").lower()  
        if salir  == "s":
            print(Fore.BLUE + Back.WHITE +"\nGracias por usar nuestra App! Vuelva pronto")
            break


# SE INVOCA A LA FUNCION PRINCIPAL
main() 