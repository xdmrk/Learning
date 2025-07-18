numeros = [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18]

def calcular_estadisticas(x):   
    
    print(f"La sumatoria de la lista es: {sum(x)}")
    
    prome = sum(x) / len(x)
    print(f"El promedio de la lista es: {prome}")
    
    print(f"el numero maximo es {max(x)}")
    
    print(f"el numero minimo es {min(x)}")
    
    print(f"La catidad de numeros en la lista es: {len(x)}")
    
resultado = calcular_estadisticas(numeros)

#Con diccionario

numeros = [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18]
print(" ")

def calcular_estadistica(x):  
    if not x:
        return "Lista vacia"
    
    estadisticas = {
        "suma" : sum(x),
        "promedio" : sum(x) / len(x),
        "maximo" : max(x),
        "minimo" : min(x),
        "cantidad" : len(x)        
    } 
    return estadisticas

numeros = [1, 44, 65, 7, 5, 34, 2, 6, 87, 6, 9, 7, 8, 78, 57, 46, 4]
resultados = calcular_estadistica(numeros)
print(resultados) #ó

for resultado in resultados:
    print(f"{resultado} : {resultados[resultado]}")
    #{resultados[resultado]} para que nos muestre el valor de la clave 
    
# ó
print(" ")

for clave, valor in resultados.items():
    print(f"{clave} : {valor}")
    
print(" ")
print(resultados.items())
#.items() para obtener los items de un diccionario


   
    