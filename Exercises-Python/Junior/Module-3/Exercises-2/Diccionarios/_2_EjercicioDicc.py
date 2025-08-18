paciente = {
    "nombre": "Carlos",
    "especie": "perro",
    "edad": 5,
    "vacunado": True
}

# Muestra cuales son las claves que tiene el diccionario paciente
print("Claves disponibles en el registro del paciente: ")
for clave in paciente.keys():
    print(clave)

# Muestra cuales son los valores que tiene el diccionario paciente
print("Valores disponibles en el registro del paciente: ")
for valor in paciente.values():
    print(valor)

# Muestra todos los pares clave - valor que tiene el diccionario paciente
print("Registro de informacion del diccionario paciente: ")
for clave, valor in paciente.items():
    print(f"clave: {clave} - valor: {valor}")


# Agregar al diccionario
paciente.update({
    "especie": "gato",
    "edad": 6
})

# Muestra todos los pares clave - valor que tiene el diccionario paciente
print("Registro de informacion del diccionario paciente: ")
for clave, valor in paciente.items():
    print(f"clave: {clave} - valor: {valor}")