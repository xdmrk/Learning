import os 

ARCHIVO_PRODUCTOS = os.path.join(os.path.dirname(__file__), "productos.txt")

# Necesario ya que me ejecutaba desde la carpeta Exercises y no desde tienda, por lo que no  encontraba el archivo
# __file__: Variable especial de Python que contiene la ruta completa del archivo actual ("C:/Users/....tienda.py)
# os.path.dirname(__file__): Extrae solo el directorio del archivo ("C:/Users/....tienda/)
# os.path.join(): Une rutas de manera inteligente, usando el separador correcto del sistema ("C:/Users/....tienda/productos.txt)


def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO_PRODUCTOS): #Este archivo existe
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                linea = linea.strip()
                if linea:
                    
                    if not linea or linea.startswith("ID#"): #Se salta la primera linea
                        continue

                    if not linea or linea.startswith("AUTO_INCREMENT"):# Se salta la ultima
                        continue

                    _id,nombre,precio,stock = linea.split("#")

                    productos.append({
                        "id": int(_id),
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock)
                    })
    return productos

print(leer_productos())

# def guardar_productos():
#     pass

# def mostrar_productos():
#     pass

# def agregar_producto():
#     pass

# def vender_producto():
#     pass

# def menu():
#     while True:
#         print(" ===== TIENDA =====")
#         print("1. Mostrar productos")