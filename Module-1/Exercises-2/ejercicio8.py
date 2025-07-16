#Verificar si un computador cumple con los requisitos mínimos: al menos 8 GB de RAM y 256 GB de almacenamiento SSD.

ram = int(input("Digite su memoria RAM: "))
ssd = int(input("Digite su almacenamiento SSD: "))

if(ram > 8 and ssd > 256):
    print("Su computador cumple con los requisitos minimos.")
else:
    print("Su computador no cumple con los requisitos minimos.")
    