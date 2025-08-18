usuarios = {
    "usuario001": {"nombre":"Pedro","telefono":564532165,"correo":"jsgfs@gmail.com","roles":["admin"]},
    "usuario002": {"nombre":"el pepe","telefono":65451,"correo":"dfhfghv@gmail.com","roles":["soporte"]},
    "usuario003": {"nombre":"camila","telefono":8765421,"correo":"jorres@gmail.com","roles":["cliente"]},
    "usuario004": {"nombre":"Indigo","telefono":12345,"correo":"sapojhdsakhf@gmail.com","roles":["cliente"]}
} # "roles":["admin"]: [] lista

print(f"Nombre del usuario: {usuarios['usuario001']["nombre"]}") # Nombre del usuario: Pedro

# Nuevo susuario
usuarios["usuario005"] = {
    "nombre":"pedrito","telefono":789654,"correo":"elpredro@gmail.com", "roles":["admin", "soporte"]
}

# Muestra todos los usuarios del diccionario y su respectivo subdiccionario
print("Usuarios registrados:")
for user_id, datos in usuarios.items():
    print(f"Usuarios: {user_id} - Informacion {datos}")

# Muestra todos los usuarios con rol "admi"
print("\nUsuarios con rol Admin")
for user_id, datos in usuarios.items():
    if "admin" in datos.get("roles", []):
        print(f"Usuario {user_id} - {datos["nombre"]}")

# Muestra los valores de cada subdiccionario y su usuario
for usuario_id, datos_usuario in usuarios.items():
    print(f"Usuario ID: {usuario_id}")
    for valor in datos_usuario.values():
        print(f"  {valor}")
    print()