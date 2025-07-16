import time 

def medir_tiempo(funcion): 
    def wrapper(*args, **kwargs): 
        inicio = time.time() 
        resultado = funcion(*args, **kwargs) 
        fin = time.time() 
        tiempo_total = fin - inicio 
        print(f"La función {funcion.__name__} tardó {tiempo_total:.4f} segundos en ejecutarse") 
        return resultado 
    return wrapper 

@medir_tiempo 
def funcion_lenta(): 
    for i in range(1000000): 
        pass 
    return "¡Listo!" 
    
@medir_tiempo 
def sumar_numeros(*numeros): 
    return sum(numeros) 


print(funcion_lenta()) 
print(sumar_numeros(1, 2, 3, 4, 5))