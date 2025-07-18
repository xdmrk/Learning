#Una tienda aplica un descuento a un producto. Se debe calcular el precio final después del descuento aplicado.

precio = float(input("Digite el valor del producto: "))
descuento = float(input("Digite el valor del porcentaje de descuento a aplicar: "))

descuento /= precio
precio -= descuento

print("El total a pagar es de ", precio, " USD")