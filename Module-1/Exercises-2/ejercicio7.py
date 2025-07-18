#Una ONG desea comparar las donaciones recibidas por parte de dos empresas y determinar si una fue mayor o si ambas fueron iguales.

don1 = float(input("Digite la donacion de la empresa 1: "))
don2 = float(input("Digite la donacion de la empresa 2: "))

if (don1 > don2):
    print("La primera empresa dono más que la segunda")
elif (don1 == don1):
    print("Ambas empresas donaron lo mismo")
else:
    print("La segunda empresa dono más que la primera")
    