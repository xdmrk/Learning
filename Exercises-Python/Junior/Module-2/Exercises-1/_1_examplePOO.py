class Persona:
    """ DOCUMENTACIÓN
    paream:
    nombre(str) = nombre del usuario
    edad(int) = edad sel usuario

    metodos:
    saludar: imprime un saludo
    """

    def __init__(self, nombre: str, edad: int): #_init_: inicializador de los atributos de la clase
        """
        Inicialiaza una nueva instancia de la calse Persona
        
        Args:
            nombre(str) = nombre del usuario
            edad(int) = edad sel usuario
        """
        
        self.nombre = nombre #Atributo
        self.edad = edad #Atributo

    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1

    def cambiar_ciudad(self, nueva_ciuda):
        self.ciudad = nueva_ciuda
        print("Se cambio la ciudad")    


class Persona2:

    def __init__(self, nombre: str, edad: int, ciudad: str):
        """
        Inicialiaza una nueva instancia de la calse Persona
        
        Args:
            nombre(str) = nombre del usuario
            edad(int) = edad sel usuario
            ciudad(str) = ciudad del usuario
        """
        self.nombre = nombre #Atributo
        self.edad = edad #Atributo
        self.ciudad = ciudad

    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y vivo en {self.ciudad}")


class Persona3:

    def __init__(self, nombre: str, edad: int):
        """
        Inicialiaza una nueva instancia de la calse Persona
        
        Args:
            nombre(str) = nombre del usuario
            edad(int) = edad sel usuario
            ciudad(str) = ciudad del usuario ya establecida
        """
        self.nombre = nombre #Atributo
        self.edad = edad #Atributo
        self.ciudad = "Bogota"

    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y vivo en {self.ciudad}")


class Persona4: #Atributos publicos, privados y protegidos

    def __init__(self, nombre: str, edad: int, ciudad: str = "Bogota"):
        """
        Inicialiaza una nueva instancia de la calse Persona
        
        Args:
            nombre(str) = nombre del usuario
            edad(int) = edad sel usuario
            ciudad(str) = ciudad del usuario por defecto bogota o la ingresada
        """
        self.nombre = nombre # Publico
        self.__edad = edad # Privado: solo se puede acceder atravez de una clase y get
        self._ciudad = ciudad # Protegido: solo se puede acceder por medio de una clase, Persona4._ciudad() no permitira obtener el atributo

    def get_edad(self): # get: acceder al atributo privado
        return self.__edad

    @property # Informa que es metodo getter
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.__edad} años y vivo en {self._ciudad}")

persona1 = Persona("Astro", 25)
persona1.saludo()

persona2 = Persona2("Camila", 26, "Cali")
persona2.saludo()

persona3 = Persona3("Cecilia", 80)
persona3.saludo()

persona4 = Persona4("Felipe", 12)
persona4.saludo()

persona5 = Persona4("Ricardo", 34, "Ibague")
persona5.saludo()

