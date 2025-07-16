#ciclo - for - yo se la cantidad de veces que se va a repetir
#bucle - while - yo NO se la cantidad de veces que se va a repetir

#FOR (para)
for i in range(0,3):
    print(i)
    
frutas = ["manzana", "pera", "fresa"]
for fruta in frutas:
    print(fruta)

#WHILE (mientras)
contador = 1 #siempre se inicializa fuera del while
while contador <=5:
    print(contador)
    
suma = 0
numero = int(input("Ingrese el numero: "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese el numero: "))#para que lo vuelva a pedir hasta que salga del bucle
    
print(f"la suma total es: {suma}")
    