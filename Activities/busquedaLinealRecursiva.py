def busquedaLinealRecuriva (A,x,st,end): #st indice menor, end indice mayor
    encontrado=-1 #valor por default para encontrado
    if st > end: #
        return -1
    else:
        if A[st] == x: #Compara el indice con el valor a encontrar
            return st #Regresa el indice en el que esta el valor encontrado
        else:
            return busquedaLinealRecuriva(A, x, st+1, end) #aumenta de indice para comparar un nuevo valor
        return encontrado

A=[3,7,2,55,3,8,45]
x=8 #Valor a encontrar
print(busquedaLinealRecuriva(A, x, 0, 6)) 