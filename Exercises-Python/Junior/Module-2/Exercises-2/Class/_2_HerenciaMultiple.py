class Volador:
    def volar(self):
        return "Puede volar"
    
class Corredor:
    def correr(self):
        return "Puede correr"
    
class Nadador:
    def nadar(self):
        return "Puede nadar"

class Perro(Corredor):
    pass

# Herencia multiple
class Pato(Volador, Corredor, Nadador):
    pass
    