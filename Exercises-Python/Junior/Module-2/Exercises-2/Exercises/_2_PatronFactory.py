class Animal:
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guaau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miauu"
    
class Pato(Animal):
    def hacer_sonido(self):
        return "Cuakk"
    
# "FABRICA" de hacer sonido: evita que se tenga que inicializar cada clase
class FabricaSonido:
    def crearSonido(self, Objeto: object):
        return Objeto()
    
fabrica = FabricaSonido()

print(fabrica.crearSonido(Gato).hacer_sonido())
    

