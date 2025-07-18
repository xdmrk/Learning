def filtrar_pares_impares(numeros):    
    pares= []
    impares= []
    
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)            
        else:
            impares.append(i)                 
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

numeros = {1,2,5,4,3,6,7,8,6,5,4,8,9,5,3,3,3,4,5,6,4,6,0}   
filtrar_pares_impares(numeros)


#clase
def filtrar_pares_impares_(numeros): 
    pares = [n for n in numeros if n % 2 == 0] 
    """
    [n:expresion de transformacion (n*2) guardaria el 2 como 4 en la lista par
    for n: iteracion, para cala elemento
    in numeros: en la lista numeros
    if n % 2 == 0: condicion]
    
    1)Ejecuta el iterador for. 
    2)verifica si cumple el if. 
    3)aplica la exprecion (primera n) de ser necesario (n*2)"""
    impares = [n for n in numeros if n % 2 != 0] 
    return pares, impares 

filtrar_pares_impares_([1, 2, 3, 4, 5, 6]) 
