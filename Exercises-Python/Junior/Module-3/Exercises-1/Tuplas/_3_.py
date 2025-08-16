def agregar_turno( turnos, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError ("Todos los campos son obligatorios")
    turnos.append([nombre.title(), dia.title(), turno.title()])

def insertar_turno(turnos, indice, nombre, dia, turno):
    if not nombre or not dia or not turno:
        raise ValueError ("Todos los campos son obligatorios")
    if indice < 0 or indice > len(turnos):
        raise IndexError (f"Indice fuera de rango {len(turnos)} turnos registrados")
    turnos.insert(indice, [nombre.title(), dia.title(), turno.title()])

def eliminarTurnoPorNombre(turnos, nombre):
    for t in turnos:
        if t[0] == nombre.title():
            turnos.remove(t)
            return
    raise ValueError(f"El empleado {nombre} no existe")

def eliminarUltimoTurno(turnos):
    if not turnos:
        raise IndexError("No hay turnos para eliminar")
    return turnos.pop()

def mostrarTurnos(turnos):
    print("\nTurnos asignados: ")
    for t in turnos:
        print((f"{t[0]} - {t[1]} - {t[2]}"))

def main():
    turnos = []

    try:
        agregar_turno(turnos, "Dayanna", "lunes", "mañana")
        agregar_turno(turnos, "andre", "jueves", "tarde")
        agregar_turno(turnos, "filip", "marTes", "tarde")
        agregar_turno(turnos, "Juan", "viernes", "noche")
        agregar_turno(turnos, "andre", "jueves", "tarde")

        insertar_turno(turnos, 1, "andre.2", "martes", "noche")
        mostrarTurnos(turnos)

        eliminarUltimoTurno(turnos)
        mostrarTurnos(turnos)


    
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()