from models.programa import Programa
from models.estudiante import Estudiante
from models.matricula import Matricula

class ControllerMatricula:
    def __init__(self):
        self.matriculas = []

    def agregarMatricula(self, matricula: Matricula):
        for matriculas in self.matriculas:
            if matriculas.id == matricula.id:
                return False
        self.matriculas.append(matricula)
        return True
    
    def mostrarMatriculas(self):
        return self.matriculas
    
    def mostrarMatriculaPorId(self, id):
        for matricula in self.matriculas:
            if matricula.id == id:
                return matricula
        return None
    
    def eliminarMatricula(self, id):
        for matricula in self.matriculas:
            if matricula.id == id:
                self.matriculas.remove(matricula)
                return True
        return None #
