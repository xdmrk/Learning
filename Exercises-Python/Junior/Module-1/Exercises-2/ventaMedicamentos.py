'''La drogueria solo maneja 3 productos fijos en el sistema, c/u tiene su propio nombre, precio e ingreso acumulado. El usuario podra
ver los productos disponibles, vender cualquiera de los 3, consultar ingresos totales, salir del sistema'''

p1 = "Acetaminofen"
precio1 = 2000
ingreso1 = 0

p2 = "Ibuprofeno"
precio2 = 3500
ingreso2 = 0

p3 = "Omeprasol"
precio3 = 6700
ingreso3 = 0

def mostrarMenu():
    print("\nMENU DROGERIA LOS ENANITOS")
    print("1. Productos disponibles")
    print("2. Vender producto")
    print("3. Ingresos totales")
    print("4. Salir")
    
def opc1():
    print("\nProductos disponibles")
    print(f"1. {p1} - ${precio1}")
    print(f"2. {p2} - ${precio2}")
    print(f"3. {p3} - ${precio3}")
    
def opc2():
    global ingreso1, ingreso2, ingreso3 #--> global: para poder manipular las variables, estara cambiando de forma global
    opc1()
    
    opcion = int(input("Ingrese el producto a vender: "))
    if opcion == 1:
        cantidad = int(input(f"Cuantos {p1} va a vender: "))
        total = cantidad * precio1
        ingreso1 += total
        print(f"Venta realizada por ${total}")
        
    elif opcion == 2:
        cantidad = int(input(f"Cuantos {p2} va a vender: "))
        total = cantidad * precio2
        ingreso2 += total
        print(f"Venta realizada por ${total}")
        
    elif opcion == 3:
        cantidad = int(input(f"Cuantos {p3} va a vender: "))
        total = cantidad * precio3
        ingreso3 += total
        print(f"Venta realizada por ${total}")
        
    else:
        print("Producto no existe")
        
def opc3():
    print(f"Total ingresos de {p1} es de ${ingreso1}")
    print(f"Total ingresos de {p2} es de ${ingreso2}")
    print(f"Total ingresos de {p3} es de ${ingreso3}")
    print(f"\nTotal ingresos es: ${ingreso1 + ingreso2 + ingreso3}")
    
while True:
    mostrarMenu()
    
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        opc1()
    elif opcion == 2:
        opc2()
    elif opcion == 3:
        opc3()
    elif opcion == 4:
        print("Adios")
        break
    else:
        print("Opcion incorrecta")