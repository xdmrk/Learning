class Estudiante:
    def __init__(self, id, documento, nombre, apellido, email):
        self.id = id
        self.documento = documento 
        self.nombre = nombre 
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f'{self.id}, {self.documento}, {self.nombre}, {self.apellido}, {self.email}'