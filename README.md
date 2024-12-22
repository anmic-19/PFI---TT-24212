# Proyecto Final Integrador - Curso Introducción a Python C24212 Talento Tech

# Gestión de Inventario de Tienda

## Descripción

Esta es una aplicación en Python que permite gestionar el inventario de una pequeña tienda. Permite realizar operaciones de registro, actualización, eliminación y visualización de productos en el inventario. Además, incluye funcionalidades para realizar búsquedas de productos y generar reportes de stock.

## Características

```bash
- **Registrar productos**: Añade nuevos productos al inventario con información como nombre, descripción, categoría, precio, cantidad, etc.
- **Mostrar productos**: Muestra todos los productos en el inventario.
- **Actualizar productos**: Modifica la información de productos existentes.
- **Eliminar productos**: Elimina productos del inventario.
- **Buscar productos**: Busca productos dentro del inventario.
- **Generar reportes de stock**: Crea un reporte de los productos con bajo stock o de todos los productos con su cantidad disponible.
```

## Requisitos

- Python 3.0
- SQLite 
- Librerías necesarias: `sqlite3`, `colorama`.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/anmic-19/PFI---TT-24212
```

### 2. Instalar dependencias

```bash
pip install colorama
```

## Uso

### 1. Iniciar la aplicación

Puedes ejecutar la aplicación con el siguiente comando:

```bash
python main.py
```

Esto iniciará la aplicación y te permitirá interactuar con ella a través de un menú de opciones.

### 2. Opciones disponibles

Una vez que inicies la aplicación, verás un menú con las siguientes opciones:

```bash
1. **Registrar producto**: Te pedirá ingresar información como nombre, descripción, categoría, precio y cantidad.
2. **Actualizar producto**: Puedes actualizar los detalles de un producto existente.
3. **Eliminar producto**: Elimina un producto de la base de datos.
4. **Mostrar todos los productos**: Muestra todos los productos registrados en el inventario.
5. **Buscar producto**: Permite buscar productos por nombre, categoría o precio.
6. **Generar reporte de stock**: Genera un reporte de productos con stock bajo o de todos los productos.
7. **Salir**: Cierra la aplicación.
```

### 3. Funciones

#### Registrar un producto:

```bash
menu_registrar_producto()
```

#### Mostrar los productos:

```bash
menu_mostrar_productos()
```

#### Actualizar un producto:

```bash
menu_actualizar_producto()
```

#### Eliminar un producto:

```bash
menu_eliminar_producto()
```

#### Buscar producto:

```bash
menu_buscar_producto()
```

#### Generar reporte de stock:

```bash
menu_reporte_bajo_stock()
```

#### Insertar productos:

```bash
db_insertar_producto()
```

#### Retornar todos los elementos: 

```bash
db_get_productos()
```

#### Retornar un elemento según su id:

```bash
db_get_producto_by_id()
```

#### Actualizar la cantidad de un elemento según un id:

```bash
db_actualizar_producto()
```

#### Eliminar un elemento según el id:

```bash
db_eliminar_producto()
```

#### Retornar mínimo stock:

```bash
db_get_productos_by_condicion()
```


## Estructura del Proyecto

```
PFI---TT-24212/
│
├── main.py              # Archivo principal de la aplicación
├── fx_db.py             # Archivo con funciones relacionadas a la base de datos
├── fx_menu.py           # Archivo con funciones del inventario
├── inventario.db        # Base de datos SQlite
└── README.md            # Documentación
``` 

## Licencia

Este proyecto fue desarrollado con sotfware Open Source.

---

Este `README` proporciona una descripción general de la aplicación, explica cómo instalarla y usarla, y también incluye detalles sobre la estructura del proyecto. 
