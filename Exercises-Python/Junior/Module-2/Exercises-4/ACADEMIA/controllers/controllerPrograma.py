from models.programa import Programa

class controllerPrograma:
    def __init__(self):
        self.programas = []

    def agregarPrograma(self, programa: Programa):
        for programa in self.programas:
            if programa.id == programa.id:
                return False
            
        self.programas.append(programa)
        return True
    
    def mostrarPrograma(self):
        for programa in self.programas:
            return programa

    def mostrarProgramaPorNombre(self, nombre):
        for programa in self.programas:
            if programa.nombre == nombre:
                return programa

    def eliminarPrograma(self, id):
        for programa in self.programas:
            if programa.id == id:
                self.programas.remove(programa)
                return True
            
    def actualizarPrograma(self, id, nombre, cohorte):
        for programa in self.programas:
            if programa.id == id:
                programa.nombre = nombre
                programa.cohorte = cohorte
                return True
