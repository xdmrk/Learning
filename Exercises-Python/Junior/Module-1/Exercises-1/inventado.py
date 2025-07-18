'''
el gobierno dara insentivos economicos a la poblacion dependiendo el estrato
1 : 1 millon
2: 500
3:200
4:0
5: impuesto 300
6: impuesto 500'
ese dinero sera aplicado para el pago de la matricula universitaria'''

#declaracion de variables
estrato = int(input("digite su estrato: "))
matricula = float(input("digite el valor de la matricula: "))

#implementacion de condicionales
if(estrato == 1):
    matricula -= 1000000
    print(f"el valor de la matricula es {matricula}")
elif(estrato == 2):
    matricula -= 500000
    print(f"el valor de la matricula es {matricula}")
elif(estrato == 3):
    matricula -= 200000
    print(f"el valor de la matricula es {matricula}")
elif(estrato == 4):
    print(f"el valor de la matricula es {matricula}")
elif(estrato == 5):
    matricula += 300000
    print(f"el valor de la matricula es {matricula}")
elif(estrato == 6):
    matricula += 500000
    print(f"el valor de la matricula es {matricula}")
else:
    print(f"el estrato {estrato} no existe")