from models.programa import Programa

class ControllerPrograma:
    def __init__(self):
        self.programas = []

    def agregarPrograma(self, programa: Programa):
        for programas in self.programas:
            if programas.id == programa.id:
                return False
        self.programas.append(programa)
        return True
    
    def mostrarProgramas(self):
        return self.programas
    
    def mostrarProgramaPorNombre(self, nombre):
        for programa in self.programas:
            if programa.nombre == nombre:
                return programa
        return None
    
    def actualizarPrograma(self, id, nombre, cohorte):
        for programas in self.programas:
            if programas.id == id:
                programas.nombre = nombre
                programas.cohorte = cohorte
                return True
        return False

    def eliminarPrograma(self, id):
        for programas in self.programas:
            if programas.id == id:
                self.programas.remove(programas)
                return True
        return False