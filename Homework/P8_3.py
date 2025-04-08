

def Central(x,y):#definiendo la funcion
    
    CifraC1= int ((A%100)/10)#determina el numero central
    print ("Primera cifra central: \n", CifraC1)
    
    CifraC2= int((B%100/10))#determina el numero central
    print ("Segunda cifra central: \n", CifraC2)
    
    suma= CifraC1 + CifraC2 #suma de los dos numeros 
    
    print("La suma de las cifras centrales es:\n", suma)
    
A =int(input("Ingrese su primer numero: \n"))
B =int(input("Ingrese su segundo numero: \n"))

Central(A,B)#entra a la funcion central 

