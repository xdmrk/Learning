from models.vehiculos import FabricaVehiculos
from views.vista import*

def iniciar_app():
    tipo = pedirTipoVehiculo()

    try:
        vehiculo = FabricaVehiculos.crear(tipo)

    except ValueError as e:
        print(e)

# CADENA DE RESPONSABILIDADES