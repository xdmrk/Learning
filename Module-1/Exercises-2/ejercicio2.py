#declarar variables
nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Tercera nota: "))

#implementar operadores
nota1 *= 0.3
nota2 *= 0.3
nota3 *= 0.4

promedio = nota1 + nota2 + nota3

print(f"el promedio es: {promedio:.2f}")