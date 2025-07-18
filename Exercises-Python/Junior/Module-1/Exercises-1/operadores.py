#Declarar variables y pedir datos por teclado
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

#Implementar operadores (aritmeticos) = Operadores de asignacion
suma = num1+num2
resta = num1-num2
mult = num1*num2
div = num1/num2
div2 = num1//num2
modu = num1%num2
potencia = num1**num2

#Salida de datos por consola
print(f"La suma es: {suma:.0f}") #elimino decimales
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {mult}")
print(f"La division es: {div}")
print(f"La division entera es: {div2}")
print(f"El modulo es: {modu}")
print(f"La potencia es: {potencia}")
