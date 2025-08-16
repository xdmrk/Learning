# Slice: obtener un subconjunto de valores de una lista

ventas_mensuales = [12_000, 5_000, 8_200, 3_400, 7_620, 10_300, 20_000, 13_600, 9_700, 15_000]
ventas_porcion1 = ventas_mensuales[1:3] # [5000, 8200]

print("Ventas de trimestre 1: ", ventas_porcion1)

ventas_top = [v for v in ventas_mensuales if v > 13_000]
#lampda function, funciones desechables
print("Ventas sobresalientes: ", ventas_top)
