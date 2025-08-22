biblioteca = {
    "autores": {
        "Gabriel Garcia Marquez": {"nacionalidad": "Colombiano"},
        "Julio Cortazar": {"nacionalidad": "Argentino"}
    },
    "libros": {
        "Cien años de soledad": {"autor": "Gabriel Garcia Marquez", "año": 1967},
        "Rayuela": {"autor": "Julio Cortazar", "año": 1963}
    },
    "prestamos": {
        "Carlos": [{
            "libro": "Cien años de soledad", "fecha": "2024-08-25"
        }]
    }
}

print(biblioteca)