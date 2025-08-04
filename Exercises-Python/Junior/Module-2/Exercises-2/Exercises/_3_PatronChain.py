class Manejador:
    def __init__(self, siguiente = None):
        self.siguiente = siguiente

    def manejo(self, solicitud):
        if self.siguiente:
            return self.siguiente.manejo(solicitud)
        return "Solicitud no atendida"
    
class SoporteBasico(Manejador):
    def manejo(self, solicitud):
        if solicitud == "preguntas generales":
            return "Soporte basico respondido"
        return super().manejo(solicitud)
    
class SoporteTecnico(Manejador):
    def manejo(self, solicitud):
        if solicitud == "preguntas tecnicas":
            return "Soporte tecnico respondido"
        return super().manejo(solicitud)
    
class SoporteEspecializado(Manejador):
    def manejo(self, solicitud):
        if solicitud == "error critico":
            return "Soporte especializado respondido"
        return super().manejo(solicitud)
    
cadena = SoporteBasico(SoporteTecnico(SoporteEspecializado()))

print(cadena.manejo("preguntas generales"))
print(cadena.manejo("preguntas tecnicas"))
print(cadena.manejo("error critico"))
print(cadena.manejo("pregunta rara"))