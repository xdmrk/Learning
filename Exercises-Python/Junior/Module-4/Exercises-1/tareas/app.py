archivo = open("tareas.txt", "w") #read, write
archivo.write("Tarea 1: Estudiar")
archivo.close()

archivo = open("tareas2.txt", "w", encoding="utf-8") #encoding para que lea la ñ y el emoji
archivo.write("Tarea 1: Estudiar ñ 🤣")
archivo.close()

tareas = ["Tarea 1: estudiar Python",
        "Tarea 2: hacer ejercicio"]

archivo = open("tareas3.txt", "w")

for tarea in tareas:
    archivo.write(tarea)
    archivo.write("\n")
archivo.close

# Lectura
'''
"r" Lectura
"w" Escritura
"a" Agregar
"r+" Lectura y escritura
'''
with open("tareas.txt") as archivo:
    lineas = archivo.readlines()
    print(lineas)

nueva_tarea = "Tarea 2: Hacer ejercicios"
with open("tareas.txt", "a") as archivo: # append: añadir
    archivo.write("\n")
    archivo.write(nueva_tarea)

# Eliminar contenido
with open("Tareas.txt", "w") as archivo:
    pass