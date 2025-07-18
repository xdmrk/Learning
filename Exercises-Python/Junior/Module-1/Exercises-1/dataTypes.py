#Declarar variables y pedir datos por teclado
edad = int(input("Cual es tu edad?: "))
salario = float(input("Cual es tu salario: "))
nombre = input("Cual es su nombre?: ")

#Salida de datos por consola
print("La edad es: ", edad)
print("El salario es: {}".format(salario)) #sale 1 decimal por defecto
print(f"El nombre es: {nombre}")

#float -->:.#f cantidad de decimales a imprimir
print(f"El salario es: {salario:.0f}")
