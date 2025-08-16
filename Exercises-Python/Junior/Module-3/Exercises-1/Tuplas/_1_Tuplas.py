def registrarEmpleado (nombre, cargo, salario):
    if not nombre or not cargo or salario <= 0:
        raise ValueError ("Datos invalidos") #Manejo de errores
    return (nombre.title(), cargo.title(), float(salario))

def mostrarEmpleados(empleados):
    print("\nRegistro de contratos laborales: ")
    for i, emp in enumerate(empleados, start=1):
        nombre, cargo, salario = emp
        print(f"{i}. {nombre} - {cargo} - ${salario:,.2f}")

def main():
    #Lista de tuplas
    empleados = []

    try:
        #tuplas
        empleados.append(registrarEmpleado("ana maria", "ingeniera", 8_500))
        empleados.append(registrarEmpleado("oScar", "matematico", 5_500)) # Oscar
        empleados.append(registrarEmpleado("funyi", "ventas", 11_500))
        empleados.append(registrarEmpleado("","ventas", 11_500))
        empleados.append(registrarEmpleado("yukimoto", "compras", -11_500))

    except ValueError as e:
        print(e)


    mostrarEmpleados(empleados)

if __name__ == "__main__":
    main()