class Vehiculo:
    def __init__(self, tipo, altura = None):
        self.tipo = tipo
        self.altura = altura

class FabricaVehiculos:

    @staticmethod
    def crear(tipo):
        if tipo == "carro":
            return Vehiculo("Carro", 1.6)
        elif tipo == "moto":
            return Vehiculo("Moto")
        elif tipo == "camion":
            return Vehiculo("Camion", 3.0)
        else:
            raise ValueError("Tipo de vehiculo no valido")