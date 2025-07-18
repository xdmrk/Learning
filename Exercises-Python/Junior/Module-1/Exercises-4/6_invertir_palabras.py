def invertir_palabras(frase):
    palabras = frase.split() #divide el texto en partes
    return ' '.join(reversed(palabras)) 

#reversed(palabras) --> recorre la lista o tupla y la itera en sentido contrario ("mundo", "Hola")
#' '.join --> une los elementos separados en una sola cadena o String (mundo Hola) con el separador ' '
    
print(invertir_palabras("Hola mundo horrible y cruel"))
    
#nuevaFrase = frase[::-1] #[start:stop:step]
#   return nuevaFrase
#print(invertir_palabras("Hola mundo horrible y cruel"))""" 
#leurc y elbirroh odnum aloH    