import sys
from controllers.controllerEstudiante import ControllerEstudiante
from models.estudiante import Estudiante
from views.vistaPrincipal import VistaPrincipal
from views.vistaEstudiante import VistaEstudiante

class AcademiaApp:
    def __init__(self):
        #Controllers
        self.controlador_estudiante = ControllerEstudiante()

        #Vista
        self.vista_principal = VistaPrincipal()
        self.vista_estudiante = VistaEstudiante()

        #Counters
        self.estudiante_id_conter = 1

    def gestion_estudiantes(self):
        while True:
            self.vista_estudiante.limpiar_pantalla()
            self.vista_estudiante.mostrar_menu_estudiante()
            opcion = self.vista_estudiante.obtener_entradas("Selecione una opcion: ")

            if opcion == "1":
                self.agregar_estudiane()
            elif opcion == '2':
                self.mostrar_estudiantes()
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass
            elif opcion == '5':
                pass
            elif opcion == '6':
                pass
            elif opcion == '0':
                break
            else:
                self.vista_estudiante.mostrar_opcion_invalida()

    def agregar_estudiane(self):
        datos = self.vista_estudiante.mostrar_formulario_agregar_estudiante()

        if datos:
            estudiante = Estudiante(self.estudiante_id_conter, datos['documento'], datos['nombre'],datos['apellido'],datos['email'])

        if self.controlador_estudiante.agregarEstudiante(estudiante):
            self.estudiante_id_conter +=1
            self.vista_estudiante.mostrar_mensaje_exito("Estudiante agregad exitosamente")
        else:
            self.vista_estudiante.mostrar_mensaje_error("Ya existe un estudiante con con ese documento o email.")
    
    def mostrar_estudiantes(self):
        estudiantes = self.controlador_estudiante.mostrarEstudiantes()
        self.vista_estudiante.mostrar_estudiantes(estudiantes)

    def ejecutar(self):
        while True:
            self.vista_principal.limpiar_pantalla()
            self.vista_principal.mostrar_menu_principal()
            opcion = self.vista_principal.obtener_entradas("Selecione una opcion: ")

            if opcion == "1":
                self.gestion_estudiantes()
            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '0':
                self.vista_principal.mostrar_mensaje_despedida()
                sys.exit(0)
            else:
                self.vista_principal.mostrar_opcion_invalida()

if __name__ == "__main__":
    app = AcademiaApp()
    try:
        app.ejecutar()
    except KeyboardInterrupt:
        print("¡Gracias por usar el sistema de Academia!")
        sys.exit(0)