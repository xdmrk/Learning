#declarar variables
#por la compra de tres productos paga 65% (descuento de 35%)
print("Ingrese los precios de los tres productos")
producto1 = float(input("Precio de producto 1: "))
producto2 = float(input("Precio de producto 2: "))
producto3 = float(input("Precio de producto 2: "))

#aplicar operadores
total = producto1 + producto2 + producto3
total *= 0.65 
#imprimir por consola
print(f"El total de su compra es: {total}USD")