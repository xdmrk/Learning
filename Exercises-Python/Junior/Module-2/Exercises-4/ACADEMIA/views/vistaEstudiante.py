from . import utils

class VistaEstudiante:
    def __init__(self):
        pass

    def limpiar_pantalla(self):
        utils.limpiar_pantalla()

    def mostrar_menu_estudiante(self):
        print("=" * 50)
        print("         GESTION DE ESTUDIANTES")
        print("=" * 50)
        print("1. Agregar Estudiante")
        print("2. Mostrar Todos los estudiantes")
        print("3. Buscar Estudiante por Documento")
        print("4. Buscar Estudiante por Email")
        print("5. Actualizar Estudiante")
        print("6. Eliminar Estudiante")
        print("0. Volver al Manu Principal")
        print("=" * 50)

    def obtener_entradas(self,mensaje):
        return utils.obtener_entrada(mensaje)
    
    def validar_email(self, email):
        return utils.validar_email(email)
    
    def mostrar_formulario_agregar_estudiante(self):
        print("--- AGREGAR ESTUDIANTE ---")

        documento = self.obtener_entradas("Documento: ")
        if not utils.validar_campo_requerido(documento,"documento"):
            return None
        
        nombre = self.obtener_entradas("Nombre: ")
        if not utils.validar_campo_requerido(nombre,"nombre"):
            return None
        
        apellido = self.obtener_entradas("Apellido: ")
        if not utils.validar_campo_requerido(apellido,"apellido"):
            return None
        
        email = self.obtener_entradas("Email: ")
        if not utils.validar_campo_requerido(email,"email") or not self.validar_email(email):
            return None
        
        return {
            'documento': documento,
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }
    
    def mostrar_estudiantes(self, estudiantes):
        print("--- ESTUDIANTE REGISTRADOS ---")

        if not estudiantes:
            utils.mostrar_lista_vacia("No hay estudiantes registrados")
        else:
            utils.mostrar_contador_registros("estudiantes",len(estudiantes))
            print(f"{'ID':<5} {'Documento':<15} {'Nombre':<20} {'Apellido':<20} {'Email':<30}" )
            print("=" * 90)
            for estudiante in estudiantes:
                print(f"{estudiante.id:<5} {estudiante.documento:<15} {estudiante.nombre:<20} {estudiante.apellido:<20} {estudiante.email:<30}")

        utils.pause_ejecucion()
        


    def mostrar_mensaje_exito(self,mensaje):
        utils.mostrar_mensaje_exito(mensaje)

    def mostrar_mensaje_error(self,mensaje):
        utils.mostrar_mensaje_error(mensaje)

    def mostrar_opcion_invalida(self):
        utils.mostrar_opcion_invalida()