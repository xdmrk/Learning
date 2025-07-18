def sumar_positivos(lista):
    return sum(filter(lambda x: x > 0, lista))

toro = (1,3,3,2,1,2,3,1,-44,-10000,3,2,9,0)
print(sumar_positivos(toro))


def suma_positivos(lista):
    return sum(x for x in lista if x > 0) #(expresión for elemento in iterable if condición)

toro = (1,3,3,2,1,2,3,1,-44,-10000,3,2,9,0,1)
print(suma_positivos(toro))

"""
    filter(
        lista: int, 
        i: >0,):
        """