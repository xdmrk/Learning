#declarar variables
print("Ingrese la produccion por turno")

turno1 = float(input("Ingrese la produccion del turno 1: "))
turno2 = float(input("Ingrese la produccion del turno 2: "))

#implementamos operadores
diferencia = turno1 - turno2

print(f"la diferencia de produccion es {diferencia}")
print("si el numero es positivo el turno 1 tuvo mayor produccion")
print("si el numero es negativo el turno 2 tuvo mayor produccion")
print("si el numero es 0 ambos turnos produjeron lo mismo")