import string

def contar_palabras_unicas(texto):
    texto = texto.lower()
    
    for i in string.punctuation: #Modulo string, punctuation: Cadena de caracteres ASCII que se consideran caracteres de puntuación
        texto = texto.replace(i, "")
        
    palabras = texto.split()    
    return f"Palabras unicas: {set(palabras)}, Total de palabras: {len(set(palabras))}" #set: almacena datos unicos(no duplicados) y desordenados
        

frase = str(input("Ingrese una cadena de texto: "))
print(contar_palabras_unicas(frase))
