class Animal: # Clase padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}"
    

class Mamifero(Animal):
    def __init__(self, nombre, edad, tiempoVida):
        super().__init__(nombre, edad)
        self.tiempoVida = tiempoVida



class Perro(Mamifero):
    def __init__(self, nombre, edad, tiempoVida, raza):
        super().__init__(nombre, edad, tiempoVida) 
        self.raza = raza
    
animal1 = Animal("Kcas", 3)
print(animal1.mostrarInformacion())

mamifero1 = Mamifero("Sushi", 1)
print(mamifero1.mostrarInformacion()) 

perro1 = Perro("Ayudante de Santa", 6, "criollo")
print(perro1.mostrarInformacion())















class Perro(Animal): # clase hija

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Llama al constructor de clase padre
        self.raza = raza

# POLIMORFISMO
    def mostrarInformacion(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, raza: {self.raza}"
    

class Gato(Animal):
    pass


animal1 = Animal("Kcas", 3)
print(animal1.mostrarInformacion())

perro1 = Perro("Ayudante de Santa", 6, "criollo")
print(perro1.mostrarInformacion())

gato1 = Gato("Sushi", 1)
print(gato1.mostrarInformacion())