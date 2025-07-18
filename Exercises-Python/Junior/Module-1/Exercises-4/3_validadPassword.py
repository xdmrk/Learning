def validar_password(password):
    if len(password) >= 8: #Verifica la longitud de password
        if any (i.isupper() for i in password): #Any: al menos uno, sea mayuscula
            if any (i.islower() for i in password): #Al menos uno sea minuscula
                if any (i.isdigit() for i in password): #Al menos uno sea digito
                    if any (i in "!@#$%^&*()" for i in password): #Al menos uno sea caracter especial
                        return "Buena contraseña"
                    else:
                        return "Debe tener al menos un caracter especial (!@#$%^&*)"                    
                else:
                    return "Debe tener al menos un digito"            
            else:
                return "Debe tener al menos una letras minuscula"            
        else:
            return "Debe tener al menos una letra mayuscula"        
    else:
        return "Debe tener al menos 8 caracteres"
    
contra = "asdfgetggG1!" #True
print(validar_password(contra))



def validar__password(password): 
    if len(password) < 8: 
        return False 
    tiene_mayuscula = False 
    tiene_minuscula = False 
    tiene_numero = False 
    tiene_especial = False 
    caracteres_especiales = "!@#$%^&*"
    
    for caracter in password: 
        if caracter.isupper(): 
            tiene_mayuscula = True 
        elif caracter.islower(): 
            tiene_minuscula = True 
        elif caracter.isdigit(): 
            tiene_numero = True
        elif caracter in caracteres_especiales: 
            tiene_especial = True 
            
    return "Buena contraseña"

print(validar__password("Abcdefg1!")) #True