saldo = 5000
historial = []
retiros = 0
depositos = 0
clave = "1234"
usuario = "root"
intentos = 3

print("Inicio de sesion")
while intentos > 0:
    
    usuariointento = input("Ingrese el usuario: ")
    claveintento = input("Ingrese la clave: ")
    
    if claveintento == clave and usuariointento == usuario: 
        print(f"\nbienvenido {usuario}")       

        while True:
            print("\n---- MENU ----")
            print("1. Ver saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Ver historial de movimientos")
            print("5. Cambiar clave")
            print("6. Salir")    
            opcion = int(input("Digite la opcion: "))
            print(" ")
            
            if opcion == 1:
                print(f"su saldo es {saldo:.2f}USD")
                
            elif opcion == 2:
                monto = float(input("Monto a retirar: "))
                if monto <= saldo:
                    saldo -= monto
                    historial.append(f"Retiraste {monto:.2f}")
                    retiros += monto
                    print(f"Retiro exitoso. saldo actual {saldo:.2f}")
                    
                else:
                    print("Saldo insuficiente")
                    
            elif opcion == 3:
                monto = float(input("Monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    historial.append(f"Depositaste {monto:.2f}")
                    depositos += monto
                    print(f"Deposito exitoso. Nuevo saldo {saldo:.2f}")
                else:
                    print(f"Deposito con valores negativos no es posible")
                
            elif opcion == 4:
                print("Historial de movimientos:")
                if len(historial) == 0:
                    print("No hay movimientos para mostrar")
                else:
                    for i in historial: #Para que recorra el arreglo y muestre todos los movimientos 
                        print(i)
                        
                    print(f"\nDepositos totales: {depositos} \nRetiros totales: {retiros}")
                
            elif opcion == 5:
                intento = input("Ingrese su clave actual: ")
                if intento == clave:
                    nueva = input("Ingresa la nueva clave: ")
                    clave = nueva
                    print("Cambio de clave exitoso")
                else:
                    print("Constraseña incorrecta")
                
            elif opcion == 6:
                print("Gracias por usar nuestro servicio")
                break
            
            else:
                print("opcion invalida")
                                
    elif intentos == 1:
        print("Acceso denegado, datos incorrectos")
        break
        
    else:
        intentos -=1
        print(f"Datos incorrectos, le quedan {intentos}")
        
