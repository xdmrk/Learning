class MotorViejo: # Codigo viejo

    def encender(self):
        return "Motor encendido"
    
class MotorNuevo: # Codigo nuevo

    def encendido(self):
        return "Motor encendido"
"""ADAPTER
sin tocar la clase MotorViejo ni el print, debemos hacer que sea la clase MotorNuevo quien responda con la funcion encendido
teniendo en cuenta que en el print la funcion que llama es encender y tampoco puede ser modificada"""


class AdapterMotor:
    def __init__(self, motor):
        self.motor = motor

    def encender(self):
        return self.motor.encendido()

motor = AdapterMotor(MotorNuevo())



print(motor.encender()) # Codigo viejo
