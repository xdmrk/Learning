from abc import ABC, abstractmethod # clase ABC: restricciones py

class Forma(ABC):
    @abstractmethod # Restriccio, calcular_area debe ser sobre escrita por algun hijo para poder ser usada
    def calcular_area(self):
        return "No deberias estar aqui"
    
    # sin el decorador se podra llamar
    def calcular_perimetro(self):
        return "No deberias estar aqui"
    

class Rectangulo(Forma):
    def calcular_area(self):
        return "Estoy calculando el are"
    
rec1 = Rectangulo()
print(rec1.calcular_area())
print(rec1.calcular_perimetro())