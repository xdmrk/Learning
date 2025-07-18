'''#funcion BASICA
def saludar():
    print("Hola")

saludar()

#funcion CON PARAMETROS
def saludarEs(nombre): #no es una variable, es un parametro, solo puede recibir informacion
    print(f"Hola {nombre}")
    
saludarEs("Sergio") #--> argumento o literal de informacion
    
#funciones COR RETORNO DE VALOR
def sumar(a , b):
    return a + b #--> retorna operacion, puede ejecutar en otro lugar

resultado = sumar(10, 8)
print(resultado)
print(sumar(10, 0))

#ejercicio

def sumaHasta100():
    total = 0
    for i in range (1, 101): #para un numero antes 
        total += i
    print(total) #--> imprime
    return total
    

print(f"La suma de 1 a 100 es: {sumaHasta100()}") #--> imprime

resultado = sumaHasta100()
print(f"La suma de 1 a 100 es: {resultado}") #--> imprime
sumaHasta100() #--> imprime por el print de la funcion'''

def validarPass():
    password = "1234"
    intentos = 0
    
    while intentos < 3:
        entrada = input("Ingrese el password: ")
        if entrada == password:
            print("bienvenido")
            return
        else:
            intentos += 1
            print(f"password incorrecto, quedan {3-intentos}")
            
            
    print("Has excedido los intentos")
    
validarPass()

        
def tablaMult(numero):
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
        
numero = int(input("Ingrese un numero: "))
tablaMult(numero)