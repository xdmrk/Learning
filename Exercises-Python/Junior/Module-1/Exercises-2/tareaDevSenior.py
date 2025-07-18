#ENUNCIADO CLASE 4
precioJ = 18000000
precioP = 18000000
precioM = 18000000
descuento = 0.10 #el descuento es del 90%, lo hacemos directo
programaJ = "Java de Cero a Senior"
programaP = "Python con IA Aplicada"
programaM = "Mobile Senior con IA"
estudiantesJ = 0
estudiantesP = 0
estudiantesM = 0
ingresosJava = 0
ingresosPython = 0
ingresosMobile = 0


def menu():
    print("MENU DEV SENIOR\n")
    print("1. Programas disponibles")
    print("2. Venta de programas")
    print("3. Ver ingresos acumulados")
    print("4. Total de ingresos")
    print("5. Salir")
    
def opc1(): #Mostrar programas
    print("\nProgramas disponibles")
    print(f"Curso {programaJ} - ${precioJ * descuento}")
    print(f"Curso {programaP} - ${precioP * descuento}")
    print(f"Curso {programaM} - ${precioM * descuento}")
    
def opc2(): #Registrar ventas
    global estudiantesJ, estudiantesP, estudiantesM, ingresosJava, ingresosPython, ingresosMobile
    
    print("\nVenta de programas")
    print(f"1. {programaJ}")
    print(f"2. {programaP}")
    print(f"3. {programaM}")
    print(f"4. Salir\n")
    opcion = int(input("Curso a vender: "))
    
    if opcion == 1:
        print(f"Venta exitosa del programa {programaJ} por un valor de ${precioJ * descuento}")
        ingresosJava += precioJ * descuento
        
        estudiantesJ += 1
        print(f"Estudiantes matriculados: {estudiantesJ}")
        
    elif opcion == 2:
        print(f"Venta exitosa del programa {programaP} por un valor de ${precioP * descuento}")
        ingresosPython += precioP * descuento
        
        estudiantesP += 1
        print(f"Estudiantes matriculados: {estudiantesP}")
        
    elif opcion == 3:
        print(f"Venta exitosa del programa {programaM} por un valor de ${precioM * descuento}")
        ingresosMobile += precioM * descuento
        
        estudiantesM += 1
        print(f"Estudiantes matriculados: {estudiantesM}")
        
    elif opcion == 4:
        menu()
        
    else:
        print("Opcion invalida")
        
def opc3(): #Ingresos por programa
    print("\nIngresos por programa")
    print(f"1. {programaJ}")
    print(f"2. {programaP}")
    print(f"3. {programaM}")
    print(f"4. Salir\n")
    opcion = int(input("Curso a conslutar: "))
    
    if opcion == 1:
        print(f"Se han vendido {estudiantesJ} cursos de {programaJ} con un ingreso acumulado de ${ingresosJava}")
    
    elif opcion == 2:
        print(f"Se han vendido {estudiantesP} cursos de {programaP} con un ingreso acumulado de ${ingresosPython}")
    
    elif opcion == 3:
        print(f"Se han vendido {estudiantesM} cursos de {programaM} con un ingreso acumulado ${ingresosMobile}")
        
    elif opcion == 4:
        menu()
        
    else:
        print("Opcion invalida")
        
def opc4(): #Mostrar ingresos totales
    print(f"El total general de ingresos hoy es de {ingresosJava + ingresosPython + ingresosMobile}")
    
while True:
    menu()
    
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        opc1()
    elif opcion == 2:
        opc2()
    elif opcion == 3:
        opc3()
    elif opcion == 4:
        opc4()
    elif opcion == 5:
        print("Adios")
        break
    else:
        print("Opcion incorrecta")
        