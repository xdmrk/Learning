class Animal: # Clase padre

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}"


class Perro(Animal):

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) 
        self.raza = raza

    # Polimorfismo sobreescritura: mantener el nombre cambiando su comportamiento
    def mostrarInformacion(self):
        return f"{super().mostrarInformacion()}, raza: {self.raza}"