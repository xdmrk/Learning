class Nadador:
    def __init__(self, nadar):
        self.nadar = nadar

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
    return objeto.nadar()

pato1 = Pato()
barco1 = Barco()
pez1 = Pez()

print(procesar_objeto_acuatico(pato1))