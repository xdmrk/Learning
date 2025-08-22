from models.estudiante import Estudiante

class ControllerEstudiante:
    def __init__(self):
        self.estudiantes = []

    def agregarEstudiante(self, estudiante: Estudiante):
        for estudiantes in self.estudiantes:
            if (estudiantes.documento == estudiante.documento) or (estudiantes.email == estudiante.email):
                return False
            
        self.estudiantes.append(estudiante)
        return True

    def mostrarEstudiantes(self):
        return self.estudiantes
        
    def mostrarEstudiantePorDocumento(self, documento):
        for estudiante in self.estudiantes:
            if estudiante.documento == documento:
                return estudiante
        return None
            
    def mostrarEstudiantePorEmail(self, email):
        for estudiante in self.estudiantes:
            if estudiante.email == email:
                return estudiante
        return None
            
    def actualizarEstudiante(self, documento, nombre, apellido):
        for estudiantes in self.estudiantes:
            if estudiantes.documento == documento:
                estudiantes.nombre = nombre
                estudiantes.apellido = apellido
                return True
        return False

    def eliminarEstudiante(self, documento):
        for estudiantes in self.estudiantes:
            if estudiantes.documento == documento:
                self.estudiantes.remove(estudiantes)
                return True
        return False
