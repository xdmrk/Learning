from . import utils

class VistaPrincipal:
    def __init__(self):
        pass

    def limpiar_pantalla(self):
        utils.limpiar_pantalla()

    def mostrar_menu_principal(self):
        print("=" * 50)
        print("         SISTEMA ACADEMIA DEV SENIOR")
        print("=" * 50)
        print("1. Gestion de Estudiantes")
        print("2. Gestion de Programas")
        print("3. Gestion de Matriculas")
        print("0. Salir")
        print("=" * 50)

    def obtener_entradas(self,mensaje):
        return utils.obtener_entrada(mensaje)
    
    def mostrar_mensaje_despedida(self):
        print("¡Gracias por usar el Sistema de Academia Dev Senior!")

    def mostrar_opcion_invalida(self):
        utils.mostrar_opcion_invalida()