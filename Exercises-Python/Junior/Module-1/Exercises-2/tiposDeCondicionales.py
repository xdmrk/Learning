#CONDICIONAL SIMPLE
edad = int(print("Digite su edad: "))
if edad > 18:
    print("Eres mayor de edad")
    
#CONDICIONAL COMPUESTA
nota = float(input("Digite su nota: "))
if nota >=3:
    print("aprovaste")
else:
    print("reprobaste")
    
#CONDICIONAL MULTIPLE
nota = float(input("Digite su nota: "))
if nota >=0 and nota < 3:
    print("reprobaste")
elif nota >= 3 and nota <=5:
    print("aprobaste")
else:
    print("error")

#CONDICIONAL ANIDADA
usuario = input("Ingrese el usuario: ")
clave = input("Ingrese la clave: ")

if usuario == "root":
    if clave == "123":
        print("Bienvenido")
    else:
        print("Clave incorrecta")
else:
    print("Usuario incorrecto")