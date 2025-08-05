import datatime

class Vehiculo:
    def __init__(self, tipo, altura, placa):
        self._tipo = tipo           # Atributos protegidos: necesitaran metodos accesores
        self._altura = altura
        self._placa = placa
        self._horaEntrada = None    # Atributo no inicializado
        self._horaSalida = None
        self._espacio = None

    @property # Metodo accesor
    def tipo(self):
        return self._tipo

    @property
    def altura(self):
        return self._altura

    @property
    def placa(self):
        return self._placa

    @property
    def horaEntrada(self):
        return self._horaEntrada

    @property
    def horaSalida(self):
        return self._horaSalida

    @property
    def espacio(self):
        return self._espacio

# CLASES HIJAS
class Carro(Vehiculo):
    def __init__(self, placa):
        super().__init__("Carro", 1.6, placa)

class Moto(Vehiculo):
    def __init__(self, placa):
        super().__init__("Moto", 1.2, placa)

class Camion(Vehiculo):
    def __init__(self, placa):
        super().__init__("Camion", 3.0, placa)

"""
De esta forma no necesitariamos clases hijas de vehiculos

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
            """

class FabricaVehiculos:
    @staticmethod
    def crear(tipo, placa):
        if tipo == "carro":
            return Carro(placa)
        elif tipo == "moto":
            return Moto(placa)
        elif tipo == "camion":
            return Camion(placa)
        else:
            raise ValueError("Tipo de vehiculo no valido")

# Tarifas fijas
class CalculadoraTarifaria: 
    def __init__(self):
        self._tarifas = {
            "carro": 2_000,
            "moto": 1_000,
            "camion": 5_000
        }

    def calcular(self, vehiculo, horaEntrada, horaSalida):
        if not horaEntrada or not horaSalida:
            return False
        
        duracion = (horaSalida - horaEntrada)
        horas = duracion.total_seconds() / 360

        horas = max(1, horas)   # Evalúa el máximo entre 1 y el valor actual de la variable horas usando la función max
                                # Si horas es menor que 1 (0, -5), el valor asignado será 1

        tipo = vehiculo.tipo.lower() # lower(): convierte a minusculas
        return self._tarifas[tipo] * horas
    
# Gestor de espacios
class Espacios:
    def __init__(self):
        self._espacios = {
            "carro": 20,
            "moto": 30,
            "camion": 5
        }

    def disponibles(self, tipo):
        # return (lambda x: False if x == 0 else x)(self._espacios[tipo])
        return self._espacios[tipo]
    
    def asignarEspacio(self, vehiculo):
        tipo = vehiculo.tipo.lower()

        if not self.disponibles(tipo):
            return False
        
        self._espacios[tipo] -= 1
        return True # Solo informa que funciona correctamente
    
    def liberarEspacio(self, vehiculo):
        tipo = vehiculo.tipo.lower()
        self._espacios[tipo] += 1
        return True
    
class RepositoryVehiculos:
    def __init__(self):
        self._vehiculos = []

    def guardar(self, vehiculo):
        self._vehiculos[vehiculo.placa] = vehiculo
        return True
    
    def obtenerXplaca(self, placa):
        return self._vehiculos.get(placa)
    
    def eliminar(self, placa):
        if placa in self._vehiculos[placa]:
            del self._vehiculos[placa]
            return True
        return False
    
    def obtenerTodos(self):
        return self._vehiculos.copy()
    
    def existePlaca(self, placa):
        return placa in self._vehiculos
    
class Parqueadero:
    def __init__(self):
        self._fabrica = FabricaVehiculos
        self._calculadora = CalculadoraTarifaria
        self._espacios = Espacios
        self._repositorio = RepositoryVehiculos

    def ingresarVehiculo(self, tipo, placa):
        try:
            if not self._espacios.disponibles(tipo):
                return False, f"No hay espacios disponibles para {tipo}"
            
            if self._repositorio.existePlaca(placa):
                return False, f"El vehiculo con placa {placa} ya se encuentra en el parqueadero"
            
            vehiculo = self._fabrica.crear(tipo, placa)

            self._espacios.asignarEspacio(vehiculo)
            
            vehiculo.horaEntrada = datatime.datetime.now()
            
            return True, f"El vehiculo tipo {tipo} con placa {placa} ingreso exitosamente"
        
        except Exception as e:
            return False, str(e)
        
    def retirarVehiculo(self, placa):
        try:
            vehiculo = self._repositorio.obtenerXplaca(placa)
            if not vehiculo:
                return False, f"El vehiculo con placa {placa} no se encuentra en el parqueadero"
            
            vehiculoLiberado = self._espacios.liberarEspacio(vehiculo)
            if vehiculoLiberado is False:
                return False, f"No se pudo liberar el espacio para el vehiculo con placa {placa}"
            
            vehiculo.horaSalida = datatime.datetime.now()
            costo = self._calculadora.calcular(vehiculo.horaEntrada, vehiculo.horaSalida)

            self._repositorio.eliminar(placa)

            return vehiculo, costo
        
        except Exception as e:
            return False, str(e)
        
    def consultarEstado(self):
        return self._repositorio.obtenerTodos()
    
    def obtenerVehiculoXplaca(self, placa):
        return self._repositorio.obtenerXplaca(placa)
        
        

            