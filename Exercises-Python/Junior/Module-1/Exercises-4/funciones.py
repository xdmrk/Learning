#funciones con parametros
def manejar_edad(edad, licencia):
    if edad >= 18 and licencia:
        print( "Puede conducir")
    elif edad < 18 and licencia:
        print("No puede conducir, es menor de edad")
    elif edad >= 18 and not licencia:
        print("No puede conducir, no tiene licencia")
    else:
        print("No puede conducir, es menor de edad y no tiene licencia")
    #Con el print se imprime en consola segun el caso que se cumpla
manejar_edad(17, False) #ya que imprime por si misma no es necesario enviar a imprimir la funcion
manejar_edad(18, True)


    
#funciones con parametros con valor por defecto
def manejar_edad_(edad, licencia = False):
    if edad >= 18 and licencia:
        return "Puede conducir"
    elif edad < 18 and licencia:
        return "No puede conducir, es menor de edad"
    elif edad >= 18 and not licencia:
        return "No puede conducir, no tiene licencia"
    else:
        return "No puede conducir, es menor de edad y no tiene licencia"
    #Con el return nos retorna un valor que debemos imprimir
sofia = manejar_edad_(19)
print(sofia)
print(manejar_edad_(20, True))


    
#funcion lambda(funcion anonima)
areaRectangulo = lambda base, altura: base * altura
print(areaRectangulo(5, 10)) 
area = areaRectangulo(5, 10)
print(area)



#Funcion de orden superior
#operar es una funcion que recibe otra funcion como argumento
def operar(f, x, y):
    return f(x, y)

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "No se puede dividir por cero"
    return x / y

opera = operar(suma, 10, 5)
print(opera)
print(operar(resta, 20, 9))



#Decorador
def mayusculas(f):
    
    def envoltura(*args, **kwargs):
        resultado = f(*args, **kwargs)
        return resultado.upper()
    return envoltura

@mayusculas
def saludar():
    return "Hola mundo"
print(saludar())

def despedir():
    return "Adioos mundo"
despedir()

mayDespe = mayusculas(despedir)
print(mayDespe())
    

"""
def despedir():
    print("Adioos mundo") #@mayusculas no funciona ya que el print retorna un None mientras el return un String
despedir()
"""
