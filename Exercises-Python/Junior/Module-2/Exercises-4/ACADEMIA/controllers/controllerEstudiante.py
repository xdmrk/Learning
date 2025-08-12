from models.estudiante import Estudiante

#clase controlador de Estudiantes
class controllerEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregarEstudiante(self, estudiante: Estudiante):
        for estudiantes in self.estudiantes:
            if (estudiantes.documento == estudiante.documento) or (estudiantes.email == estudiante.email):
                return False
            
        self.estudiantes.append(estudiante)
        return True

    def mostrarEstudiantes(self):
        for estudiante in self.estudiantes:
            return estudiante
        
    def mostrarEstudiantePorDocumento(self, documento):
        for estudiante in self.estudiantes:
            if estudiante.documento == documento:
                return estudiante
            
    def mostrarEstudiantePorEmail(self, email):
        for estudiante in self.estudiantes:
            if estudiante.email == email:
                return estudiante
        
    def actualizarEstudiante(self, documento, estudiante: Estudiante):
        for estudiantes in self.estudiantes:
            if estudiantes.documento == documento:
                estudiantes.documento = estudiante.documento
                estudiantes.nombre = estudiante.nombre
                estudiantes.apellido = estudiante.apellido
                estudiantes.email = estudiante.email
                return True
    
    def eliminarEstudiante(self, documento):
        for estudiante in self.estudiantes:
            if estudiante.documento == documento:
                self.estudiantes.remove(estudiante)
                return True


