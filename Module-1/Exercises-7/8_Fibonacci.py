def fibonacci(*args):
    if len(args) == 1:
        
        for i in args: #i toma el valor del numero almacenado en la tupla args
        #for i in range(*args) --> *args desempaqueta la tupla pero no se puede operar por lo que imprimiria hasta un numero antes del ingresado
        #por esto se le asigna el valor de la tupla a un iterador para luego que este iterador pueda ser iterado y operado
           
            for num in range (i + 1):
                print(num) 
        
    elif len(args) == 2:
        pri, seg = args #desempaqueta los dos numeros y les asigna variable
        
        while pri <= (seg + 1): #(seg + 1): para que imprima el siguiente numero mayor al segundo
            print(pri)
            pri +=1
        
    elif len(args) == 3:
        pri, seg, ter = args
        
        for i in range(pri, seg + 1, ter):
            print(i)
        #de cualquier forma debemos asignarle variables a los elementos de la tupla args, el for sirve ya que range(inicio, fin, secuencia)
        """while pri <= seg:
            print(pri)
            pri += ter"""
        
    else:
        print("Debe ingresar entre uno y tres numeros")
        
            

fibonacci(9,14, 2)