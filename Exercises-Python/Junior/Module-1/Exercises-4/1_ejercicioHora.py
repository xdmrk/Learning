from datetime import datetime

"""def saludar_persona(nombre, hora = datetime.now().hour):
#No funciona ya que la hora quedaria establecida al momento de crear la funcion"""
def saludar_persona(nombre, hora = None):
    
    if hora is None:
        hora = datetime.now().hour #Muestra la hora en entero
    
    if 5 < hora < 12:
        print(f"¡Buenos dias {nombre}!")
    elif 12 <= hora < 19:
        print(f"¡Buenas tardes {nombre}!")
    else:
        print(f"¡Buenas noches {nombre}!")
        
        
hola = saludar_persona("xdmrk")
saludar_persona("Maria", 19)
"""print(saludar_persona("Maria", 19)) --> imprime Buenas noches Maria y un None ya que no tenemos un return en la funcion y la estamos imprimiendo
podemos o cambiar los print de la funcion por return o no imprimir la funcion y solo llamarla: saludar_persona("Maria", 19)"""

#Para su comprobacion:
print(datetime.now().strftime("%I:%M:%S %p")) #Muestra la hora 24h con minutos, :%S segundos
"""%I formato de 12h, %p AM o PM """