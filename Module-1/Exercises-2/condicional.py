'''TOMA DE DECISIONES 
if(condicion)
    INSTRUCCIONES

elif(condicion)
    INSTRUCCIONES
    
else: #final
    INSTRUCCIONES
'''

numero = int(input("digite el numero: "))

#tomar decisiones (condicionales) - estructuras de control

if(numero > 0):
    print(f"el {numero} es positivo")
elif(numero < 0):
    print(f"el {numero} es negativo")
else:
    print(f"el {numero} es nulo")