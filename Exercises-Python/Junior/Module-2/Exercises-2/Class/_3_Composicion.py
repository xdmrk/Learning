class Motor:
    def arrarcar(self):
        return "Motor arranca"
    
class CocheXx(Motor):
    pass    
"""
clase Motor no es Coche por lo que no puede ser ni hija ni padre
Igualmente con clase Coche"""


# COMPOSICION 
class Coche:
    def __init__(self):
        self.motor = Motor() # Un coche TIENE un motor
    
