def menu():
    print("Tipo de vehiculo")
    print("1. Carro")
    print("2. Moto")
    print("3. Camion")
    print("0. Salir")


def pedirTipoVehiculo():
    while True:
        menu()
        opcion = input("Seleccione una opcion (1-4)").strip()
        if opcion == "1":
            return "carro"
        elif opcion == "2":
            return "moto"
        elif opcion == "3":
            return "camion"
        elif opcion == "4":
            return False
        else: 
            print("Opcion invalida")


def mostrar(resultados):
    print(resultados)


def despedida():
    print("Gracias por usar el sistema de parqueadero, Hasta pronto")