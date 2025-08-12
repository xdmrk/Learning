class Estudiante:
    # Inicializador
    def __init__(self, id, documento, nombre, apellido, email):
        self.id = id
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self): # Muestra el objeto como lo escribimos, no la referencia de memoria del objeto mismo como seria sin el __str__
        return f'{self.nombre} {self.apellido}, {self.documento}, {self.id}, {self.email} '

    # Logica del negocio
