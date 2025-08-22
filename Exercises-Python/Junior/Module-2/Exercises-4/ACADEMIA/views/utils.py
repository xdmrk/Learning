import os
import sys

def limpiar_pantalla():
    """Limpia la pantalla de terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_entrada(mensaje):
    while True:
        try:
            return input(mensaje).strip()
        except KeyboardInterrupt:
            print("\n Operacíon cancelada por el usuario")
            sys.exit(0)

def validar_email(email):
    return '@' in email and '.' in email

def validar_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def convertir_a_entero(valor, valor_por_defecto=None):
    try:
        return int(valor)
    except ValueError:
        return valor_por_defecto
    
def mostrar_mensaje_exito(mensaje):
    print(f"✅ {mensaje}")
    input("\nPresione Enter para contuniar....")

def mostrar_mensaje_error(mensaje):
    print(f"❌ Error: {mensaje}")
    input("\nPresione Enter para contuniar....")

def mostrar_mensaje_info(mensaje):
    print(f"ℹ️ Info: {mensaje}")
    input("\nPresione Enter para contuniar....")

def mostrar_mensaje_advertencia(mensaje):
    print(f"⚠️ Advertencia: {mensaje}")
    input("\nPresione Enter para contuniar....")

def mostrar_opcion_invalida():
    print(f"❌  Opcion no valida. Intente de nuevo.")
    input("\nPresione Enter para contuniar....")

def mostrar_confirmacion(mensaje):
    repuesta = obtener_entrada(f"{mensaje} (s/n): ")
    return repuesta.lower() in ['s','si','sí', 'y','yes']

def mostrar_tabla_encabezado(titulo, columnas):
    print(f"---- {titulo.upper()} ----")
    print(columnas)
    print("-" * len(columnas))

def mostrar_lista_vacia(mensaje):
    print(f"📭 {mensaje}")

def validar_campo_requerido(valor, nombre_campo):
    if not valor or not valor.strip:
        mostrar_mensaje_error(f"El campo {nombre_campo} es obligatorio.")
        return False
    return True

def mostrar_contador_registros(tipo, cantidad):
    if cantidad == 0:
        print(f"📭 No hay {tipo} registrados.")
    elif cantidad == 1:
        print(f"📋 Se encontro 1 {tipo}")
    else:
        print(f"📋 Se encontron {cantidad} {tipo}")

def pause_ejecucion():
    input("Presone Enter para continuar....")