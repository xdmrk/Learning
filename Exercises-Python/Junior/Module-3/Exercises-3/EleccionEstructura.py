# ELECCION DE LA ESTRUCTURA ADECUADA
# Lista de autores (Ordenada, puede repetirse)
autores = ["Gabriel Marquez", "Julio Cortazar", "Gabriel Marquez"]
print(autores)

# Conjunto de autores (unicidad garantizada)
autores_unicos = set(autores)
print(autores_unicos)

# Diccionario Libro y autor
libros = {
    "Cien años de soledad": "Gabriel Marquez",
    "Rayuela": "Julio Cortazar"
}
print(libros)

# ESTRUCTURAS ANIDADAS
biblioteca = {
    "libros": [
        {"titulo": "Cien años de soledad", "autor": "Gabriel Marquez", "año": "1967"},
        {"titulo": "Rayuela", "autor": "Julio Cortazar", "año": "1963"}
    ],
    "prestados": [
        {"libro": "Cien años de soledad", "usuario": "carlos", "fecha": "2024-12-01"}
    ]
}
print(biblioteca)