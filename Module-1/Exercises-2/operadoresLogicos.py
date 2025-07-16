'''dev senior en el examen pide que sus alumnos sean calificados 
con tres examenes de peso diferente (30, 40, 30)% si su promedio es
entre 0 y 2.9 reprueba, 3 y 5 aprueba si es mayor o menor a esas notas eeror'''

#declaracion de variables
ca1 = float(input("Digite la primera nota: "))
ca2 = float(input("Digite la segunda nota: "))
ca3 = float(input("Digite la tercera nota: "))

#implementar operaciones
ca1 *= 0.30
ca2 *= 0.40
ca3 *= 0.30

promedio = ca1 + ca2 + ca3

#condicionales
if(promedio >= 0 and promedio < 3):
    print(f"Su promedio es {promedio}, REPROBO")
elif(promedio >= 3 and promedio <= 5):
    print(f"Su promedio es {promedio}, APROBO")
else:
    print("error en ingreso de notas")