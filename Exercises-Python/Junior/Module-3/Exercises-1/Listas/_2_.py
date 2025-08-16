def mostrarCliente(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def agregarCliente(lista_clientes, nombre):
    # Validacion de datos de entrada

    # isinstance: si la (variable: tipoDato) entonces:
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title()) # .title() "luis" a "Luis"
        print(f"cilente {nombre.title()} agregado") # title nuevamente ya que no muestra el dato guardado sino la variable que entro
    else:
        print("Nombre invalido.")
        

def modificarCliente(lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <=50):
        print("Nombre invalido")
        return
    if 0 <= indice <= len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente original {original} fue modificado por {nuevo_nombre.title()}")
    else:
        print("Indice fuera de rango")

def main(): #Metodo principal, llama o habilita instancia del programa
    clientes = ["Ana", "Maria", "David"]

    print("Clientes actuales: ")
    mostrarCliente(clientes)

    agregarCliente(clientes, "indigo")
    mostrarCliente(clientes)

    modificarCliente(clientes, 0, "Catalina")
    mostrarCliente(clientes)

if __name__ == "__main__":
    main() # punto de inicio