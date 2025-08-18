# Pasar lista a diccionario
ventas = [
    ("V001", "Luis Rojas", 350000),
    ("V002", "Ana Torres", 580000),
    ("V003", "Carlos Diaz", 420000)
]

ventas_dic = {
    id_venta: {
        "cliente": cliente,
        "monto": monto
    }
    for id_venta, cliente, monto in ventas
}

print("Ventas registradas:")
for id_venta, datos in ventas_dic.items():
    print(f"ID ventas: {id_venta}")
    print(f" Cliente: {datos['cliente']}")
    print(f" Monto: ${datos['monto']:,}")
    print()