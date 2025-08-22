class Matricula:
    def __init__(self, id, id_estudiante, id_matricula):
        self.id = id
        self.id_estudiante = id_estudiante
        self.id_matricula = id_matricula

    def __str__(self):
        return f'{self.id}, {self.id_estudiante}, {self.id_matricula}'