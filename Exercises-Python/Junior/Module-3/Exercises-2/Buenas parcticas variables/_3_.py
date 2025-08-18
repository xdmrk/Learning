def mostrar_inventario(inventario: dict):
    if not inventario:
        print("Inventario vacio")
        return
    for id_producto, datos in inventario.items():
        print(f"ID: {id_producto}: Nombre: {datos['nombre']} - Precio {datos['precio']} - cantidad: {datos['cantidad']}")

def buscar_producto(inventario: dict, id_producto: str):
    producto = inventario.get(id_producto)
    if producto:
        print(f"El producto {producto} fue encontrado")
    else:
        print(f"Producto {producto} no encontrado")

def eliminar_producto(inventario: dict, id_producto: str):
    eliminado = inventario.pop(id_producto, None) # None: Si no lo consigue no hace nada
    if eliminado:
        print(f"El producto {eliminado['nombre']} fue eliminado con exito")
    else:
        print(f"El producto no fue encontrado")

def actualizar_stock(inventario: dict, id_producto: str, nueva_cantidad: float):
    if id_producto in inventario:
        inventario[id_producto]['cantidad'] = nueva_cantidad
        print("Stock actualizado")
    else:
        print("Producto no encontrado")

def limpiar_inventario(inventario: dict):
    inventario.clear()
    print("Stock en blanco")

def main():
    inventario = {
        "P001": {"nombre": "Laptop Lenovo", "precio" : 3500.00, "cantidad": 5},
        "P002": {"nombre": "mouse Logitech", "precio" : 1500.00, "cantidad": 55},
        "P003": {"nombre": "Teclado mecanico", "precio" : 400.00, "cantidad": 15}
    }

    mostrar_inventario(inventario)
    buscar_producto(inventario, "P002")
    buscar_producto(inventario, "P003")
    eliminar_producto(inventario, "P001")
    mostrar_inventario(inventario)
    actualizar_stock(inventario, "P001", 50000)
    mostrar_inventario(inventario)
    limpiar_inventario(inventario)
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()