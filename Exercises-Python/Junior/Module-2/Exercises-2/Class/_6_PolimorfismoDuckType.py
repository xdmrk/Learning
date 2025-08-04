class Pato:
    def nadar(self):
        return "El pato nada"

class Barco:
    def nadar(self):
        return "El barco nada"

class Pez:
    def nadar(self):
        return "El pez nada"


# Funcion que usa Duck
def procesar_objeto_acuatico(objeto):
    return objeto.nadar() # Llamara la funcion nadar de cada objeto

pato1 = Pato()
barco1 = Barco()
pez1 = Pez()

print(procesar_objeto_acuatico(pato1))
print(procesar_objeto_acuatico(barco1))
print(procesar_objeto_acuatico(pez1))