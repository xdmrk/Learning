# Transformacion y limpieza
datos_inconsistentes = [
    {"book": "Rayuela", "author": "Julio cortázar", "date": "1963"},
    {"book": "  Cien años de soledad", "author": "gabriel marquez", "date": "1967"},
    {"book": "Rayuela", "author": "Julio Cortázar", "date": "1963"}
]
print(datos_inconsistentes)

# Refactorizacion limpia
def limpiar_datos(datos):
    estructura_limpia = []
    vistos = set()

    for d in datos:
        libro = d["book"].strip()
        autor = d["author"].title().strip() # Normalizar nombres
        anio = int(d["date"])

        # Generar clave unica para cada libro
        clave = (libro, autor, anio)
        if clave not in vistos:
            vistos.add(clave)
            estructura_limpia.append({
                "titulo": libro,
                "autor": autor,
                "año": anio
            })
    return estructura_limpia
biblioteca_limpia = limpiar_datos(datos_inconsistentes)
print(biblioteca_limpia)