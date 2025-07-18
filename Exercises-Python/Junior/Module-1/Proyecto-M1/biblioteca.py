from prettytable import PrettyTable #Install for termianñ

#Base de datos en memoria
libros = [    
    {
        'titulo': "los cabellos ROJOS",
        'autor': "pepo",
        'isbn': "1",
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    },
    {
        'titulo': "los cabellos negRos",
        'autor': "pepx",
        'isbn': "2",
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    },
    {
        'titulo': "los cabellos AZules",
        'autor': "pepu",
        'isbn': "3",
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    },
    {
        'titulo': "los cabellos Verdes",
        'autor': "pepi",
        'isbn': "4",
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    },
    {
        'titulo': "los cabellos bLAncos",
        'autor': "pepe",
        'isbn': "5",
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    },
    {
        'titulo': "los cabellos MoRaDo",
        'autor': "pepa",
        'isbn': "6",
        'estado': 'Prestado 🚧',
        'socio_prestado': "1"        
    }
] 
socios = [
     {
        'nombre': 'Ana López Pérez',
        'identificacion': "1",
        'fecha': '2022-11-30',
        'estado': 'Activo'
    },
    {
        'nombre': 'Carlos el Curioso',
        'identificacion': '2',
        'fecha': '2023-10-05',
        'estado': 'Activo'
    },
    {
        'nombre': 'Diana Princess',
        'identificacion': '3',
        'fecha': '2023-07-18',
        'estado': 'Activo'
    },
    {
        'nombre': 'Error 404',
        'identificacion': '4',
        'fecha': '2023-09-01',
        'estado': 'Eliminado 💀'
    },
    {
        'nombre': 'Elsa Frozen',
        'identificacion': '5',
        'fecha': '2023-12-24',
        'estado': 'Activo'
    },
    {
        'nombre': 'Tony Stark',
        'identificacion': '6',
        'fecha': '2023-04-30',
        'estado': 'Activo'
    },
    {
        'nombre': 'Usuario Nuevo',
        'identificacion': '7',
        'fecha': '2023-10-20',
        'estado': 'Activo'
    }
]

def verMenu(): #muestra opciones del menu
    print("\nMINIBIBLIOTECA")
    print("1. Registrar Libro")
    print("2. Registrar un Socio")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Ver Libros Prestados")
    print("6. Ver todos los Libros")
    print("7. Ver todos los Socios")
    print("0. Salir") #Por experiencia de desarrollo
    
#Opciones del menu    
def registrar_libro():
    global libros #llamamos la lista libros
    print("Digite 0 si desea regresar al menu")
    print("\n---------------------- \(._.\ )")
    print("REGISTRO DE LIBROS\n")
    
    
    titulo = input("titulo del libro: ").strip().lower() #strip(): quita espacios al principio y al final, lower(): convierte en minuscula
    if titulo == "0":
        return
    if not titulo:
        print("El titulo no puede estar vacio")
        return
        
    autor = input("Autor del libro: ").strip().lower()
    if not autor:
        print("El autor no puede estar vacio")
        return
        
    isbn = input("ISBN del libro: ").strip().lower()
    if not isbn:
        print("El ISBN no puede estar vacio")
        return
    
    for l in libros: #Verifica si ya existe el libro a registrar
        if l['isbn'] == isbn:
            print(f"Ya existe un libro con el ISBN {isbn}")
            return
    
    #Creacion de nuevo libro
    nuevo_libro = { #diccionario, no una lista[] ya que los datos deben ingresarse de forma ordenada
        'titulo': titulo,
        'autor': autor,
        'isbn': isbn,
        'estado': 'Disponible ✅',
        'socio_prestado': None        
    }
    
    libros.append(nuevo_libro) #Agrega el diccionario nuevo_libro a la lista libros
    print(f"{titulo} de {autor}, ISBN: {isbn}")
    print("Registrado exitosamente")
    
def registrar_socio():
    global socios #llamamos la lista socios
    print("Digite 0 si desea regresar al menu")
    print("\n---------------------- \(._.\ )")
    print("REGISTRO DE SOCIOS\n")
    
    
    nombre = input("nombre completo: ").strip().lower() #strip(): quita espacios al principio y al final, lower(): convierte en minuscula
    if nombre == "0":
        return
    if not nombre:
        print("El nombre no puede estar vacio")
        return
    
    identificacion = input("Numero de identificacion: ").strip().lower()
    if not identificacion:
        print("El numero de identificacion no puede estar vacio")
        return
        
    fecha = input("fecha de nacimiento (DD/MM/AAAA): ").strip().lower()
    if not fecha:
        print("La fecha de nacimiento no puede estar vacio")
        return
    
    for cc in socios: #Verifica si ya existe el socio a registrar
        if cc['identificacion'] == identificacion:
            print(f"Ya existe un socio con el documento de identificacion {identificacion}")
            return
    
    #Creacion de nuevo socio
    nuevo_socio = { 
        'nombre': nombre,
        'identificacion': identificacion,
        'fecha': fecha,
        'estado': 'Activo'      
    }
    
    socios.append(nuevo_socio) #Agrega el diccionario nuevo_socio a la lista socios
    print(f"{nombre} con documento de identificacion {identificacion} y fecha de nacimiento {fecha}")
    print("Creado exitosamente")
    
def prestar_libro():
    global libros
    global socios
    print("Digite 0 si desea regresar al menu")
    print("\n---------------------- \(._.\ )")
    print("PRESTAMO DE LIBROS\n")
    
    prestamo = input("Ingrese el ISBN del titulo a solicitar: ").strip().lower()
    if prestamo == "0":
        return
    if not prestamo:
        print("El ISBN no puede estar vacio")
        return
    
    for l in libros: #Verifica si existe el ISBN en la lista libros
        if l['isbn'] == prestamo and l['estado'] == "Disponible ✅":
            print(f"Libro {l['titulo']} disponible para prestamo")
            
            opcion = input(f"\nSolicitar prestamos (s/n): ").strip().lower() #Confirmacion del prestamo
            if opcion in ("s", "si", "sí"):
                prestadoA = input("Ingrese el documento del socio que solicita el libro: ").strip().lower()
                
                if not prestadoA:
                    print("Debe estar inscrito para solicitar libros prestados.")
                    inscribir = input("Desea inscribirse a la red de socios de MINIBIBLIOTECA? (s/n): ").strip().lower()
                    
                    if inscribir in ("s", "si", "sí"):
                        registrar_socio() #Funcion registrar nuevo socio
                    return # <--Cualquier otra respuesta 
                
                for s in socios: #Validacion si el solicitante es socio activo para el prestamo
                    if s['identificacion'].lower() == prestadoA:
                        l['estado'] = 'Prestado 🚧'
                        l['socio_prestado'] = prestadoA
                        print(f"Libro {l['titulo']} del autor {l['autor']}, ISBN {l['isbn']} prestado correctamente")
                        return
                    
                # Si no existe el socio, da la opcion de registrarse 
                print(f"El documento de identificacion {prestadoA} no esta asociado a ningun socio existente")
                inscribir = input("Desea inscribirse a la red de socios de MINIBIBLIOTECA? (s/n): ").strip().lower()
                
                if inscribir in ("s", "si", "sí"):
                    registrar_socio()
                return
            
            return
            
        if l['isbn'] == prestamo and l['estado'] == "Prestado 🚧":
            print(f"El libro {l['titulo']} actualmente se encuentra en prestamo")
            return

    print(f"El ISBN {prestamo} no esta disponible aun en la MINIBIBLIOTECA")
    return
    
def devolver_libro():
    global libros
    global socios
    print("Digite 0 si desea regresar al menu")
    print("\n---------------------- \(._.\ )")
    print("PRESTAMO DE LIBROS\n")
    
    devolver = input("Ingrese el ISBN del libro en prestamo a devolver: ").strip().lower()
    if devolver == "0":
        return    
    if not devolver:
        print("El ISBN no puede estar vacio")
        return
    
    for l in libros:
        if l['isbn'] == devolver and l['estado'] == "Disponible ✅":
            print(f"{l['titulo']} del autor {l['autor']}, ISBN {l['isbn']} no se encuentra en prestamo para devolución")
            return
    
        if l['isbn'] == devolver and l['estado'] == "Prestado 🚧":
            print(f"Devolución del titulo {l['titulo']} del autor {l['autor']}, ISBN {l['isbn']} realizado correctamente")
            l['estado'] = "Disponible ✅"
            l['socio_prestado'] = None
            return            
        
    print(f"El ISBN {devolver} no existe en la base de datos de la MINIBIBLIOTECA")
    return

def libros_prestados():
    print(" ")
    
    tablaa = PrettyTable() #En cada función donde se llama la libreria PrettyTable, se le a puesto un nombre independiente para evitar conflictos y que sea independiente cada fncion
    tablaa.field_names = ["Titulo", "Autor", "ISBN", "Prestado a"]
    
    tablaa.title = "LIBROS PRESTADOS DE MINIBIBLIOTECA 📚"
    
    for l in libros:
        if l['estado'] == 'Prestado 🚧':
            tablaa.add_row([l["titulo"], l["autor"], l["isbn"], l['socio_prestado']])
                
    print(tablaa)

def ver_todos_libros():
    '''print("\n---------------------- \(._.\ )")
    print("TODOS LOS LIBROS\n")
    
    if not libros:
        print("No hay libros registrados en la MINIBIBLIOTECA")
        return
    
    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro['titulo']} del autor {libro['autor']}")
        print(f"ISBN: {libro['isbn']}     ---> {libro['estado']}\n")'''
        
    print(" ")
        
    table = PrettyTable()
    table.field_names = ["Titulo", "Autor", "ISBN", "Estado"]
    
    table.title = "LIBROS DE MINIBIBLIOTECA 📚"
    
    '''for i, libro in enumerate(libros, 1):
    podria utilizarlo para enumerar dentro de la tabla:
    
    table.field_names = ["#", "Titulo", "Autor", "ISBN", "Estado"]
    for i, libro in enumerate(libros, 1):
        table.add_row([i, libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])    
    '''
    
    for libro in libros:
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])
                
    print(table)

def ver_todos_socios():    
    print(" ")
    
    recuadro = PrettyTable()
    recuadro.field_names = ["Nombre", "Identificacion", "Estado"]
    
    recuadro.title = "SOCIOS DE MINIBIBLIOTECA 😏"
    
    for cc in socios:
        recuadro.add_row([cc["nombre"], cc["identificacion"], cc["estado"]])
        recuadro.add_divider() #lineas entre socio  
        
    print(recuadro)   


def main(): #funcion principal, estructura
    while True:
        verMenu()
        opcion = input("Digite la opcion (0 - 7): ").strip()
        #.strip() para quitar espacios y devolver un String
        
        '''
        Opcion de condicionales
        if opcon == '1':
            pass'''

        match opcion:
            case '1':    
                registrar_libro()
            case '2':    
                registrar_socio()
            case '3':    
                prestar_libro()
            case '4':    
                devolver_libro()
            case '5':    
                libros_prestados()
            case '6':    
                ver_todos_libros()
            case '7':    
                ver_todos_socios()
            case '0':    
                print("Gracias por usar MINIBIBLIOTECA")
                print("Hasta pronto 🧑🏼‍🏫")
            case _:    
                print("Opccion invalida, digite una opcion valida (0 - 7)")
        
main()